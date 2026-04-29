#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PLA Extract - 聚合物配方抽取工具

此脚本专注于从论文JSON数据中提取聚合物配方和加工工艺信息。
使用LLM进行多步抽取和精炼。
"""

import os
import re
import json
import time
import random

import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from google.api_core import client_options

# 导入提示词模板
from prompts import (
    MAJOR_POLYMER_EXTRACTION,
    MAJOR_POLYMER_EXTRACTION_REFINEMENT,
    PRINTING_OPTIMIZATION_EXTRACTION,
    PRINTING_OPTIMIZATION_EXTRACTION_REFINED,
)

# ============================================================================
# 配置常量
# ============================================================================

import os
from dotenv import load_dotenv
load_dotenv()
API_KEYS = [k.strip() for k in os.getenv("PLA_API_KEYS", "").split(",") if k.strip()]
LLM_API_MODEL_NAME = "gemini-2.5-flash-lite-preview-09-2025"

# 全局变量用于API Key轮换
current_key_index = 0


# ============================================================================
# LLM 模型初始化
# ============================================================================

def init_model(api_key):
    """
    初始化LLM模型
    
    Args:
        api_key: API密钥
    
    Returns:
        四个chat实例: coarse_extraction, coarse_extraction_refinement, 
                     optimization_extraction, optimization_refine
    """
    genai.configure(
        api_key=api_key,
        transport="rest",  # 建议在使用代理时强制使用 REST
        client_options=client_options.ClientOptions(
            api_endpoint="https://api.openai-proxy.org/google"
        )
    )
    
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "application/json",
    }
    
    safety_settings = {
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    }
    
    # Step 1: 粗抽取模型
    coarse_extraction_model = genai.GenerativeModel(
        model_name=LLM_API_MODEL_NAME,
        generation_config=generation_config,
        safety_settings=safety_settings,
        system_instruction=MAJOR_POLYMER_EXTRACTION,
    )
    coarse_extraction = coarse_extraction_model.start_chat()
    
    # Step 2: 粗抽取精炼模型
    coarse_extraction_refinement_model = genai.GenerativeModel(
        model_name=LLM_API_MODEL_NAME,
        generation_config=generation_config,
        safety_settings=safety_settings,
        system_instruction=MAJOR_POLYMER_EXTRACTION_REFINEMENT,
    )
    coarse_extraction_refinement = coarse_extraction_refinement_model.start_chat()
    
    # Step 3: 优化抽取模型
    optimization_extraction_model = genai.GenerativeModel(
        model_name=LLM_API_MODEL_NAME,
        generation_config=generation_config,
        safety_settings=safety_settings,
        system_instruction=PRINTING_OPTIMIZATION_EXTRACTION,
    )
    optimization_extraction = optimization_extraction_model.start_chat()
    
    # Step 4: 优化精炼模型
    optimization_refine_model = genai.GenerativeModel(
        model_name=LLM_API_MODEL_NAME,
        generation_config=generation_config,
        safety_settings=safety_settings,
        system_instruction=PRINTING_OPTIMIZATION_EXTRACTION_REFINED,
    )
    optimization_refine = optimization_refine_model.start_chat()
    
    print(f"[init_model] 模型使用新的API Key({api_key[:20]}...)初始化完毕！")
    
    return coarse_extraction, coarse_extraction_refinement, optimization_extraction, optimization_refine


# ============================================================================
# 辅助函数
# ============================================================================

def switch_to_next_key():
    """
    轮换到下一个 API Key，并重新初始化模型
    """
    global current_key_index
    
    current_key_index = (current_key_index + 1) % len(API_KEYS)
    init_model(API_KEYS[current_key_index])
    print("[switch_to_next_key] 已切换到下一个 Key，索引 =", current_key_index)


def handle_rate_limit_error(error_msg, retry_count):
    """
    处理429限流错误，智能等待和重试
    """
    # 尝试从错误信息中提取重试延迟时间
    delay_match = re.search(r'retry_delay.*?seconds: (\d+)', str(error_msg))
    
    if delay_match:
        suggested_delay = int(delay_match.group(1))
        # 使用建议的延迟时间，但加一些随机性
        wait_time = suggested_delay + random.uniform(5, 15)
    else:
        # 如果没有建议延迟，使用指数退避策略
        wait_time = min(60, (2 ** retry_count) + random.uniform(1, 5))
    
    print(f"⏰ API限流，等待 {wait_time:.1f} 秒后重试...")
    time.sleep(wait_time)
    
    # 立即切换API Key，不要等待多次重试
    switch_to_next_key()


def extract_formulations(data):
    """
    从JSON数据中提取聚合物配方列表
    
    匹配包含以下字段的配方对象:
    - id: 配方编号
    - description: 配方描述
    - polymerMatrix: 聚合物基体信息
    - fillers: 填料列表
    - additives: 添加剂列表
    - processing: 加工工艺信息
    - properties: 材料性能
    """
    formulations_list = []

    def recurse_extract(obj):
        if isinstance(obj, dict):
            # 检查是否为有效的聚合物配方对象
            if ('id' in obj and 
                'description' in obj and 
                'polymerMatrix' in obj and 
                'fillers' in obj and 
                'additives' in obj and 
                'processing' in obj and 
                'properties' in obj):
                formulations_list.append(obj)
            else:
                for key in obj:
                    recurse_extract(obj[key])
        elif isinstance(obj, list):
            for item in obj:
                recurse_extract(item)

    # 支持传入 JSON 字符串或已解析的字典/列表
    if isinstance(data, str):
        parsed_data = json.loads(data)
    else:
        parsed_data = data
    
    recurse_extract(parsed_data)
    return formulations_list


def count_non_empty_values(d):
    """
    递归计算有效键值对的数量
    """
    if isinstance(d, dict):
        return sum(count_non_empty_values(v) for v in d.values())
    elif isinstance(d, list):
        return sum(count_non_empty_values(i) for i in d)
    elif d not in ["unknown", [], {}, "", None]:
        return 1
    return 0


def extract_text_from_response(response):
    """
    从LLM响应中提取文本内容
    """
    if hasattr(response, 'candidates') and response.candidates:
        for candidate in response.candidates:
            if hasattr(candidate, 'content') and hasattr(candidate.content, 'parts'):
                for part in candidate.content.parts:
                    if hasattr(part, 'text'):
                        return part.text
    return "No valid response received."


# ============================================================================
# 主处理函数
# ============================================================================

def process_article_from_json(article_data):
    """
    从JSON格式的文章数据中抽取配方信息
    
    Args:
        article_data: 文章数据字典
    
    Returns:
        包含所有抽取信息的字典
    """
    coarse_extraction, coarse_extraction_refinement, optimization_extraction, optimization_refine = init_model(API_KEYS[0])

    text_content_JSON = json.dumps(article_data, indent=4)
    article = f'"""\n{text_content_JSON}\n"""'

    # Step 1: 粗抽取
    coarse_extraction_result = coarse_extraction.send_message(article)

    time.sleep(1)

    # Step 2: 精炼抽取结果
    user_instruction_coarse_extraction_refinement = f"""
    You will be provided with the pre-extracted JSON formatted results and the full text of the research paper. Your task is to refine the pre-extracted data according to the guidelines outlined above.
    Pre-Extracted Data:
    {extract_text_from_response(coarse_extraction_result)}
    Full Text of the Research Paper:
    {article}
    1. Verify that the paper is focused on 3D printing experiments directly related to the main topic (e.g., additive manufacturing, material formulation, printing processes, or printed part properties).
    2. Ensure that each 3D printing system has complete and specific information about the material formulation (e.g., base materials, fillers, binders, additives), printing process parameters (e.g., printing technique, nozzle size, temperature, speed, layer thickness, curing or post-processing conditions), and resulting properties. All information must be explicitly mentioned in the provided literature.
    3. Check if any 3D printing system contains materials or components represented only by numbers, symbols, or alphanumerical codes (e.g., "Material A", "Sample 1", "Resin R3") and exclude such systems.
    4. Correctly categorize the formulation components (e.g., polymer matrix, filler, reinforcement, binder, solvent, additive), the printing and post-processing parameters, and the measured properties.
    5. Provide the refined JSON formatted results according to the specified format.
    6. It should be noted that the number of 3D printing systems in a paper must be based on the actual literature and can range from 0 to 5. This number must not be fabricated. If more than 5 distinct 3D printing systems are described, only the top 5 most important systems should be reported. The value of num_3d_printing_system should be equal to the number of 3D printing systems listed below.
    7. Ensure that all 3D printing systems are consolidated into a single unified list, sharing one is_3d_printing_study and one num_3d_printing_system field. The response should contain only one instance of the is_3d_printing_study and num_3d_printing_system fields.
    """

    coarse_extraction_refinement_result = coarse_extraction_refinement.send_message(user_instruction_coarse_extraction_refinement)

    time.sleep(1)

    print_recipe_list = extract_formulations(extract_text_from_response(coarse_extraction_refinement_result))

    # print("main_print_recipe json_list", extract_text_from_response(coarse_extraction_refinement_result))

    all_print_recipe_info = {
        "article_information": json.loads(text_content_JSON),
        "main_print_recipe": json.loads(extract_text_from_response(coarse_extraction_refinement_result)),
        "print_recipe_optimization": []
    }

    # 检查数量，配方太多可能不是重点
    if len(print_recipe_list) > 5:
        limit_print_recipe = print_recipe_list[:4]
    else:
        limit_print_recipe = print_recipe_list

    print(f"该文献有{len(limit_print_recipe)}个配方")
    
    MAX_REACTION_RETRIES = 4
    found = False
    
    for print_recipe in limit_print_recipe:
        reaction_tries = 0

        while True:
            try:
                found = True

                extraction_message = f"""
                Specified reaction:
                {json.dumps(print_recipe, indent=2)}

                Based on the information in the following paper, you need to extract the process parameters and properties corresponding to the specified formula above and complete the code for that formula:
                {article}
                """
                print_recipe_optimization_result = optimization_extraction.send_message(extraction_message)

                specified_print_recipe_optimization = extract_text_from_response(print_recipe_optimization_result)

                refine_message = f"""
                        Specified reaction:
                        {specified_print_recipe_optimization}

                        Based on the information in the following paper, you need to extract details corresponding to the specified formula above and fill in the missing details in the formula.
                        {article}
                        """
                refined_details = optimization_refine.send_message(refine_message)
                
                # 将优化后的结果添加到列表中
                all_print_recipe_info["print_recipe_optimization"].append(
                    json.loads(extract_text_from_response(refined_details))
                )
                
                break  # 成功处理，跳出while循环
                
            except Exception as e:
                reaction_tries += 1
                print(f"处理反应时出错: {e}，切换到下一个 Key 并重试... (第 {reaction_tries} 次)")

                switch_to_next_key()

                if reaction_tries >= MAX_REACTION_RETRIES:
                    print(f"[WARNING] 该 reaction 连续失败 {reaction_tries} 次，放弃此 reaction。")
                    # 直接 break 掉这个 while True，跳过当前 reaction
                    break

    if found:
        return all_print_recipe_info
    else:
        return {
            "article_information": json.loads(text_content_JSON),
            "main_print_recipe": json.loads(extract_text_from_response(coarse_extraction_refinement_result)),
            "print_recipe_optimization": []
        }


# ============================================================================
# 主入口
# ============================================================================

def main():
    """
    主入口函数
    """
    input_file = "doi_details_all.json"
    output_file = "doi_details_all_extracted.json"

    with open(input_file, 'r', encoding='utf-8') as f:
        articles = json.load(f)

    if not isinstance(articles, list):
        raise ValueError("输入JSON应为列表结构")

    # 增量写入：若已有输出文件，读取已处理的 DOI，避免重复
    existing_results = []
    processed_dois = set()
    if os.path.exists(output_file):
        with open(output_file, 'r', encoding='utf-8') as f:
            existing_results = json.load(f)
        if isinstance(existing_results, list):
            for item in existing_results:
                if isinstance(item, dict):
                    doi = item.get("article_information", {}).get("doi")
                    if doi:
                        processed_dois.add(doi)

    to_process = articles
    results = existing_results if isinstance(existing_results, list) else []

    for idx, article_data in enumerate(to_process, start=1):
        doi = article_data.get("doi")
        if doi and doi in processed_dois:
            print(f"[{idx}] 跳过已处理 DOI: {doi}")
            continue

        print(f"[{idx}] 处理中 DOI: {doi or 'unknown'}")
        result = process_article_from_json(article_data)
        results.append(result)

        if doi:
            processed_dois.add(doi)

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)

    print("抽取完成，结果已保存到:", output_file)


if __name__ == "__main__":
    main()
