
from __future__ import annotations

import json
import re
import time
import hashlib
from pathlib import Path
import requests

# =========================
# 0) 路径与参数配置
# =========================

# 目标 DOI
DOI_LIST_INLINE = [
    "10.4028/www.scientific.net//Users/tthu/Desktop/高分子/dataextracion/paper/polymers-14-02721-v2",
]

# MinerU 的输出根目录 (根据用户文件位置)
MD_ROOT = Path("/Users/tthu/Desktop/高分子/dataextracion/paper")

# 最终合并后的 JSON 输出位置
OUTPUT_JSON = MD_ROOT / "/Users/tthu/Desktop/高分子/dataextracion/paper/polymers-14-02721-v2" / "/Users/tthu/Desktop/高分子/dataextracion/paper/polymers-14-02721-v2.json"

# Crossref 缓存目录
CACHE_DIR = Path("/Users/tthu/Desktop/高分子/dataextracion/crossref_cache")
CACHE_DIR.mkdir(parents=True, exist_ok=True)

MAILTO = "example@example.com" 

TIMEOUT = 20
MAX_RETRIES = 3
SLEEP_SECONDS = 0.2

# =========================
# 2. Crossref 获取出版信息
# =========================

CROSSREF_API = "https://api.crossref.org/works/{}"

def doi_cache_path(doi: str) -> Path:
    # 用 hash 做文件名，避免 DOI 中的特殊字符
    h = hashlib.sha1(doi.encode("utf-8")).hexdigest()
    return CACHE_DIR / f"{h}.json"

def load_cache(doi: str):
    path = doi_cache_path(doi)
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        if payload.get("doi") == doi:
            return payload.get("message")
    except Exception:
        return None
    return None

def save_cache(doi: str, msg):
    path = doi_cache_path(doi)
    payload = {"doi": doi, "message": msg}
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

def extract_authors(msg: dict) -> list[str]:
    authors = []
    for a in msg.get("author", []) or []:
        given = (a.get("given") or "").strip()
        family = (a.get("family") or "").strip()
        name = (a.get("name") or "").strip()
        if family and given:
            authors.append(f"{family}, {given}")
        elif family:
            authors.append(family)
        elif name:
            authors.append(name)
    return authors

def date_parts_to_str(parts) -> str:
    if not parts:
        return ""
    first = parts[0]
    if not isinstance(first, list):
        return ""
    if len(first) == 1:
        return f"{first[0]}"
    if len(first) == 2:
        return f"{first[0]}-{first[1]:02d}"
    if len(first) >= 3:
        return f"{first[0]}-{first[1]:02d}-{first[2]:02d}"
    return ""

def extract_pub_date(msg: dict) -> str:
    for key in ("published-print", "published-online", "issued"):
        if key in msg:
            parts = msg.get(key, {}).get("date-parts")
            return date_parts_to_str(parts)
    return ""

def strip_xml_tags(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", "", text)
    return text.strip()

def extract_pub_info(doi: str, msg: dict) -> dict:
    title_list = msg.get("title", []) or []
    journal_list = msg.get("container-title", []) or []
    return {
        "title": title_list[0] if title_list else "",
        "journalName": journal_list[0] if journal_list else "",
        "authors": extract_authors(msg),
        "pubDate": extract_pub_date(msg),
        "citations": msg.get("is-referenced-by-count"),
        "doi": doi,
        "abstract": strip_xml_tags(msg.get("abstract", "")),
    }

def get_crossref(doi: str, session: requests.Session, mem_cache: dict):
    if doi in mem_cache:
        return mem_cache[doi]

    cached = load_cache(doi)
    if cached is not None:
        mem_cache[doi] = cached
        return cached

    url = CROSSREF_API.format(requests.utils.quote(doi))
    headers = {}
    if MAILTO:
        headers["User-Agent"] = f"get_article/1.0 (mailto:{MAILTO})"

    last_err = None
    for _ in range(MAX_RETRIES):
        try:
            resp = session.get(url, headers=headers, timeout=TIMEOUT)
            if resp.status_code == 200:
                msg = resp.json().get("message", {})
                save_cache(doi, msg)
                mem_cache[doi] = msg
                return msg
            last_err = f"HTTP {resp.status_code}"
        except Exception as exc:
            last_err = str(exc)
            print(exc)
        time.sleep(SLEEP_SECONDS)

    print(f"Crossref 失败: {doi} -> {last_err}")
    return None

# =========================
# 3. 读取 MinerU Markdown 并组装 JSON
# =========================

def doi_to_slug(doi: str) -> str:
    doi = doi.strip()
    doi = re.sub(r"[<>:\"/\\|?*\s]+", "_", doi)
    while "__" in doi:
        doi = doi.replace("__", "_")
    return doi.strip("_")

def find_markdown(doi: str, md_root: Path) -> Path | None:
    # 特别针对用户的文件路径 /Users/tthu/Desktop/高分子/dataextracion/paper//Users/tthu/Desktop/高分子/dataextracion/paper/polymers-14-02721-v2/full.md
    if "/Users/tthu/Desktop/高分子/dataextracion/paper/polymers-14-02721-v2" in doi:
         specific_path = md_root / "/Users/tthu/Desktop/高分子/dataextracion/paper/polymers-14-02721-v2" / "full.md"
         if specific_path.exists():
             return specific_path

    slug = doi_to_slug(doi)
    candidates = [
        md_root / slug / "auto" / f"{slug}.md",
        md_root / slug / f"{slug}.md",
    ]
    for p in candidates:
        if p.exists():
            return p

    extra_dir = md_root / slug
    if extra_dir.exists():
        extra = list(extra_dir.rglob("*.md"))
        if extra:
            return extra[0]
    return None

def is_table_line(line: str) -> bool:
    s = line.strip()
    if not s or "|" not in s:
        return False
    if re.match(r"^\|?[-: ]+\|[-|: ]+\|?$", s):
        return True
    return s.count("|") >= 2

def split_markdown(text: str) -> tuple[list[str], list[str]]:
    paragraphs = []
    tables = []
    buf = []
    table_buf = []

    def flush_para():
        if buf:
            paragraphs.append(" ".join(buf).strip())
            buf.clear()

    def flush_table():
        if table_buf:
            tables.append("\n".join(table_buf).strip())
            table_buf.clear()

    for line in text.splitlines():
        if is_table_line(line):
            flush_para()
            table_buf.append(line.rstrip())
            continue

        if line.strip() == "":
            flush_table()
            flush_para()
            continue

        flush_table()
        buf.append(line.strip())

    flush_table()
    flush_para()
    return paragraphs, tables

def build_records(dois: list[str]) -> list[dict]:
    session = requests.Session()
    mem_cache = {}
    records = []

    for idx, doi in enumerate(dois, start=1):
        print(f"Processing {doi}...")
        msg = get_crossref(doi, session, mem_cache)
        pub_info = extract_pub_info(doi, msg or {})

        md_path = find_markdown(doi, MD_ROOT)
        if md_path is None:
            print(f"找不到 Markdown: {doi}")
            paragraphs, tables = [], []
        else:
            print(f"Found Markdown: {md_path}")
            text = md_path.read_text(encoding="utf-8", errors="ignore")
            paragraphs, tables = split_markdown(text)

        article_info = {
            "title": pub_info.get("title", ""),
            "journalName": pub_info.get("journalName", ""),
            "authors": pub_info.get("authors", []),
            "pubDate": pub_info.get("pubDate", ""),
            "citations": pub_info.get("citations"),
            "doi": doi,
            "abstract": pub_info.get("abstract", ""),
            "paragraphs": paragraphs,
            "figureCaptions": [],
            "schemeCaptions": [],
            "tables": tables,
        }

        records.append({
            "id": idx,
            "article_information": article_info,
        })

    return records

# =========================
# 4. OCR 清洗
# =========================

IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^\)]+\)")
HTML_TABLE_RE = re.compile(r"<\s*table\b", re.IGNORECASE)
HTML_TAG_RE = re.compile(r"</?[^>]+>")
REF_HEAD_RE = re.compile(
    r"^\s*#?\s*(references|references and notes|bibliography|literature cited)\b",
    re.IGNORECASE,
)
FIG_RE = re.compile(r"^\s*(fig\.|figure)\b", re.IGNORECASE)
TABLE_RE = re.compile(r"^\s*(table|tab\.)\b", re.IGNORECASE)
ACK_RE = re.compile(r"\backnowledg", re.IGNORECASE)
KEYWORDS_RE = re.compile(r"^\s*key\s*words?:", re.IGNORECASE)
SUPP_RE = re.compile(r"\b(supporting information|supplementary)\b", re.IGNORECASE)
FRONT_MATTER_RE = re.compile(
    r"\b(received|accepted|available online|published online|"
    r"corresponding author|e-?mail|fax|tel\.?|copyright|\(c\))\b",
    re.IGNORECASE,
)
AFFILIATION_RE = re.compile(
    r"\b(department of|university of|institute of|college of|faculty of|"
    r"school of|laboratory|centre|center)\b",
    re.IGNORECASE,
)

LATEX_CMD_KEEP = {
    "mathrm", "mathbf", "pmb", "mathsf", "mathfrak", "boldsymbol",
    "text", "textbf", "textsf", "texttt", "rm", "bf", "it", "sf", "bar",
}

GREEK_MAP = {
    "Alpha": "Alpha", "Beta": "Beta", "Gamma": "Gamma", "Delta": "Delta",
    "Epsilon": "Epsilon", "Zeta": "Zeta", "Eta": "Eta", "Theta": "Theta",
    "Iota": "Iota", "Kappa": "Kappa", "Lambda": "Lambda", "Mu": "Mu",
    "Nu": "Nu", "Xi": "Xi", "Omicron": "Omicron", "Pi": "Pi",
    "Rho": "Rho", "Sigma": "Sigma", "Tau": "Tau", "Upsilon": "Upsilon",
    "Phi": "Phi", "Chi": "Chi", "Psi": "Psi", "Omega": "Omega",
    "alpha": "alpha", "beta": "beta", "gamma": "gamma", "delta": "delta",
    "epsilon": "epsilon", "zeta": "zeta", "eta": "eta", "theta": "theta",
    "iota": "iota", "kappa": "kappa", "lambda": "lambda", "mu": "mu",
    "nu": "nu", "xi": "xi", "omicron": "omicron", "pi": "pi",
    "rho": "rho", "sigma": "sigma", "tau": "tau", "upsilon": "upsilon",
    "phi": "phi", "chi": "chi", "psi": "psi", "omega": "omega",
}

def is_reference_like(text: str) -> bool:
    if re.search(r"\[\d+\]", text):
        return True
    if re.match(r"^\s*\d+\.", text):
        return True
    if re.search(r"\b\d{4}\b", text) and text.count(";") >= 1:
        return True
    if re.search(r"\b\d{4}\b", text) and re.search(
        r"\bJ\.|\bChem\.|\bOrg\.|\bInorg\.|\bCommun\.", text
    ):
        return True
    return False

def is_non_content(text: str) -> bool:
    if len(text) < 3:
        return True
    letters = re.findall(r"[A-Za-z]", text)
    if not letters and len(text) < 10:
        return True
    return False

def collapse_spaced_letters(text: str) -> str:
    def _join(match):
        return re.sub(r"\s+", "", match.group(0))
    return re.sub(r"\b(?:[A-Za-z]\s+){2,}[A-Za-z]\b", _join, text)

def strip_latex(text: str) -> str:
    text = text.replace("\xa0", " ")
    text = re.sub(r"\\begin\{[^}]+\}", "", text)
    text = re.sub(r"\\end\{[^}]+\}", "", text)
    text = re.sub(r"\\left\s*", "", text)
    text = re.sub(r"\\right\s*", "", text)
    text = re.sub(r"\$\$(.*?)\$\$", r"\1", text)
    text = re.sub(r"\$(.*?)\$", r"\1", text)

    for cmd in LATEX_CMD_KEEP:
        pattern = re.compile(rf"\\{cmd}\s*\{{([^}}]+)\}}")
        while True:
            new_text = pattern.sub(r"\1", text)
            if new_text == text:
                break
            text = new_text

    text = re.sub(
        r"\\(bf|it|rm|sf|mathsf|mathrm|mathbf|boldsymbol|pmb|textsf|texttt)\b",
        "", text,
    )
    text = re.sub(r"\\([A-Za-z]+)\b", lambda m: GREEK_MAP.get(m.group(1), m.group(1)), text)
    text = text.replace(r"\cdot", " ")
    text = text.replace(r"\pm", "+/-")
    text = text.replace(r"\times", "x")
    text = text.replace(r"\circ", "deg")
    text = text.replace(r"\prime", "'")
    text = text.replace(r"\%", "%")
    text = text.replace(r"\_", "_")
    text = text.replace(r"\^", "^")
    text = text.replace(r"\~", " ")
    text = text.replace(r"\&", "&")
    text = re.sub(r"\\[,;:]", " ", text)
    text = re.sub(r"\\([,.;:%])", r"\1", text)
    text = re.sub(r"\\\^circ", "deg", text)
    text = re.sub(r"\\\^", "^", text)
    text = re.sub(r"\\\*", "*", text)
    text = text.replace("^circ", "deg")
    text = re.sub(r"\bleft\s*([\(\[\{])", r"\1", text)
    text = re.sub(r"\bright\s*([\)\}\]])", r"\1", text)
    text = re.sub(r"\bbegin\s+array\b", "", text)
    text = re.sub(r"\bend\s+array\b", "", text)
    text = re.sub(r"\bbegin\s+array\s+[a-zA-Z]\b", "", text)
    text = re.sub(r"\bend\s+array\s+[a-zA-Z]\b", "", text)
    text = re.sub(
        r"\b(textrm|scriptsize|scriptstyle|displaystyle|thinspace|qquad|quad|"
        r"overline|underline|cdot|nabla|widetilde|textsf|texttt|phantom|"
        r"mathtt|mathbb|mathsf|mathfrak|mathcal|bullet|dot)\b",
        "", text,
    )
    text = re.sub(r"[_^]\s*\{\s*([^}]+)\s*\}", lambda m: m.group(0)[0] + m.group(1), text)
    text = text.replace("{", " ").replace("}", " ")
    text = re.sub(r"\s*_\s*", "_", text)
    text = re.sub(r"\s*\^\s*", "^", text)
    text = re.sub(r"\\\s+", " ", text)
    text = collapse_spaced_letters(text)
    text = re.sub(
        r"\b(?:[A-Za-z]\s+){1,}[A-Za-z](?=_[0-9])",
        lambda m: re.sub(r"\s+", "", m.group(0)),
        text,
    )
    text = re.sub(r"(?<=\d)\s+(?=\d)", "", text)
    text = re.sub(r"\s*~\s*", " ", text)
    text = re.sub(r"(?<=\s)\^(\d+)\b", r"\1", text)
    text = re.sub(r"\b([A-Za-z])\s*\^\s*prime\b", r"\1'", text)
    text = re.sub(r"\b([A-Za-z]+)\s*\^\s*prime\b", r"\1'", text)
    text = re.sub(r"([a-z]{3,})_([0-9])", r"\1 \2", text)
    text = re.sub(r"\bcirc\b", "deg", text)
    text = re.sub(r"\bcirc_?C\b", "deg C", text)
    text = re.sub(r"\b(hphantom|vphantom)\b", "", text)
    text = text.replace("textmu", "u")
    return text

def clean_paragraphs(paragraphs, tables):
    new_paras = []
    new_tables = list(tables)
    total = len(paragraphs)
    in_refs = False
    drop_tail = False

    for idx, raw in enumerate(paragraphs):
        if not isinstance(raw, str):
            continue
        text = IMAGE_RE.sub("", raw).strip()
        
        if HTML_TABLE_RE.search(text):
            new_tables.append(text)
            continue
        if HTML_TAG_RE.search(text):
            text = HTML_TAG_RE.sub("", text).strip()
        
        text = strip_latex(text)
        if not text:
            continue

        if REF_HEAD_RE.search(text):
            if total > 0 and idx >= int(total * 0.6):
                drop_tail = True
                break
            in_refs = True
            continue

        if in_refs:
            if is_reference_like(text):
                continue
            in_refs = False

        if ACK_RE.search(text):
            continue
        if KEYWORDS_RE.search(text):
            continue
        if SUPP_RE.search(text):
            continue
        if FRONT_MATTER_RE.search(text):
            if len(text) < 200:
                continue
        if AFFILIATION_RE.search(text) and len(text) < 120:
            continue
        if TABLE_RE.search(text):
            new_tables.append(text)
            continue
        if FIG_RE.search(text):
            continue
        if is_non_content(text):
            continue

        new_paras.append(text)

    return new_paras, new_tables

# =========================
# Main Execution
# =========================

if __name__ == "__main__":
    # 1. Build initial records
    records = build_records(DOI_LIST_INLINE)
    
    # 2. Clean records
    for rec in records:
        article = rec.get("article_information", {})
        paragraphs = article.get("paragraphs") or []
        tables = article.get("tables") or []

        new_paras, new_tables = clean_paragraphs(paragraphs, tables)
        article["paragraphs"] = new_paras
        article["tables"] = new_tables

    # 3. Save
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Done! Saved to {OUTPUT_JSON}")
