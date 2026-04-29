# 文献解析与数据提取逻辑

> 基于 `mineru_pdf_parser.py` 和 `0120_get_doi_detail_electrolyte.ipynb` 文件的两种文献解析流程梳理

---

## 📋 概述

本模块支持两套不同源的文献内容及结构解析工作流，最终输出统一规范的数据结构，旨在为后续的大模型 (LLM) 实验及配方数据抽取（见 `extraction_logic.md`）提供干净、结构化的纯净上下文信息。这两套工作流分别针对 **PDF 文档源** 和 **HTML 网页源**：
1. **工作流 1 (PDF 源)**：基于 MinerU 对 PDF 的 OCR 和版面分析结果 (Markdown) 进行正则清洗和排版还原。
2. **工作流 2 (HTML 源)**：基于提前爬取的各出版社底层原网页 HTML 源码，结合定制化的 CSS 选择器实现结构化数据的精准截取。

所有处理流均通过 **Crossref API** 统一获取并对齐文献的基础元数据（标题、作者、发表日期、引文量、摘要等）。

---

## 🔄 解析流程总览

```
               输入: 文献 DOI
                      │
           [Crossref API 获取元数据]
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
   【方法一: PDF 解析】         【方法二: HTML 解析】
    (convert_msf.py)       (0120_get_doi_detail.ipynb)
          │                       │
 ┌─────────────────┐     ┌─────────────────┐
 │ 1.读取MinerU MD │     │ 1.从Minio读取HTML │
 │ 2.段落/表格拆分 │     │ 2.匹配出版商选择器│
 │ 3.去除图表与非内│     │ 3.精细抽取段落且分│
 │   容噪声文本    │     │   离图/表标题     │
 │ 4.LaTeX公式清洗 │     │ 4.关联正文内引用  │
 └────────┬────────┘     └────────┬────────┘
          │                       │
          └───────────┬───────────┘
                      ▼
            【统一规范 JSON 数据结构】
```

---

## 📄 方法一：基于 PDF 和 MinerU 的解析提取

**源文件:** `mineru_pdf_parser.py` (PDF到Markdown解析), `convert_msf.py` (数据清洗与结构化)
**适用场景:** 针对缺乏良好 HTML 数据源，仅能获取到 PDF 格式文件的文献。

### 使用方法

1. **执行 PDF 格式转换**：
   使用 `mineru_pdf_parser.py` 解析本地 PDF 文件。脚本将调用 API 进行全文本分析，并下载包含 Markdown 结果的数据包。
   ```bash
   python mineru_pdf_parser.py <pdf_path>
   ```
2. **清洗与结构化抽取**：
   配置并运行 `convert_msf.py`。该脚本会自动加载前一步生成的 Markdown 文件，并连接 Crossref 补齐文献元数据，随后一键将内容清洗、切割，最终输出为规范的结构化 JSON 数据集合供下游使用。

---

## 🌐 方法二：基于 HTML 网页源码的直接解析

**源文件:** `0120_get_doi_detail_electrolyte.ipynb`

### 数据来源

文本内容源自 Web of Science (WoS) 数据库。通过高级检索过滤出核心文献，随后该程序成功读取并解析输出了 **2146** 篇具备极高研究相关性的 HTML 格式文献内容。

所采用的检索规则为：
```text
TS = (
  ("polylactic acid" OR PLA)
  AND
  ("fused deposition modeling" OR FDM OR "3D printing")
  AND
  (composite* OR filler* OR reinforcement*)
)
```

### 使用方法

本方法主要通过自动化批量脚本执行完成：

1. **准备清单**：确保工作区具备需要拉取的 DOI 列表（如 `downloaded_doi_0120.json`）。
2. **批量抽取**：直接在 Jupyter 环境中打开并顺次运行 `0120_get_doi_detail_electrolyte.ipynb` 内的代码块。脚本将自动从云端加载原网页并执行精确截取。
3. **获取输出**：代码执行完毕后，将自动生成高度纯化的文献集合 JSON 文件（如 `doi_details_all.json`），即拿即用。

---

## 📦 最终对齐输出：结构化文献载体

无论来源和最初的加工技术路径如何，文献数据在清洗阶段的终点都将被封装为统一的基于 Python Dictionary 并导出的 JSON 数据对象 `ArticleInformation`。这将作为上下文核心交付给最终的大模型，执行配方的结构化提纯。

| 字段名 | 类型 | 说明 |
|--------|------|------|
| `doi` | string | 文献唯一标识符 |
| `title` | string | 论文标题 |
| `journalName` | string | 期刊名称缩写/全称 |
| `authors` | string[] | 作者列表 |
| `pubDate` | string | 发表日期 |
| `citations` | number | 过往被引总量 |
| `abstract` | string | 摘要 |
| `paragraphs` | string[] | **正文核心段落数组** |
| `figureCaptions` | string[] | 图注长文本集合 |
| `schemeCaptions` | string[] | 方案图注文集合 |
| `tables` | mixed array | 表格结构体描述内容 |

---

---
基本信息：
3D打印领域文献（3484，20260120）：https://www.webofscience.com/wos/alldb/summary/5f2c0bf0-1e6d-4fcb-b084-152831da1024-0198116ee6/relevance/1
Minio bucket: electrolyte-brain

访问方式：
下载这一链接中的ipynb脚本后使用colab打开：
https://git.xmu.edu.cn/ChenWeifeng/paper-crawler/-/blob/main/electrolyte-brain-doi-0120/0120_get_doi_detail_electrolyte.ipynb
设置colab的secret项：
GITLAB_TOKEN: glpat-yB6zhpJu1bCKftYKO76yim86MQp1OjF3bQk.01.0z1vypxf2

AKA: nUr1BhhXwDBH282sluDv

SK: yttWzyGi3xxFEyhV4otL7flKynqqMM5TLiKmgeHQ

进度：
目前已爬取（2576/3484）
- 存在273个缺失doi的结果
- 剩余文献未提供网页版，或没有访问权限
