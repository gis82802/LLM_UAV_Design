# api_server_multi_llm.py

import asyncio
import uvicorn
import os
import json
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Dict, Any, AsyncGenerator
from dotenv import load_dotenv 

from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM, ChatOllama
from langchain_openai import ChatOpenAI 
from langchain_core.language_models.base import BaseLanguageModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

from rag_handler import RAGHandler
from config import MODEL_CONFIGURATIONS
from prompts import (
    TRANSLATION_PROMPT_TEMPLATES,
    CONVERSATION_SUMMARY_PROMPT,
    MISSION_ANALYSIS_PROMPT,
    QUERY_ANALYSIS_PROMPT,
    UNIFIED_RAG_PROMPT
)

load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
print = logging.info

def get_model(model_config: Dict[str, Any]) -> BaseLanguageModel:
    model_type = model_config.get("type")
    model_name = model_config.get("model_name")
    base_url = model_config.get("base_url")
    print(f"    - Factory creating: type='{model_type}', name='{model_name}', base_url='{base_url}'")
    
    if model_type == "ollama":
        mode = model_config.get("mode", "chat")
        print(f"      - Ollama mode: '{mode}'")
        params = {"model": model_name, "request_timeout": 300.0, "base_url": base_url}
        if "options" in model_config and isinstance(model_config["options"], dict):
            extra_options = model_config["options"]
            print(f"      - Applying Ollama options: {extra_options}")
            params.update(extra_options)
        if mode == "completion":
            return OllamaLLM(**params)
        else:
            return ChatOllama(**params)
    elif model_type == "proxy":
        api_key_env = model_config.get("api_key_env")
        api_key = os.getenv(api_key_env)
        if not api_key:
            raise ValueError(f"API key not found. Please set the environment variable '{api_key_env}' in your .env file.")
        print(f"      - Proxy mode using OpenAI client. Key found in '{api_key_env}'.")
        return ChatOpenAI(model_name=model_name, openai_api_base=base_url, openai_api_key=api_key, temperature=0.0, request_timeout=300.0)
    else:
        raise ValueError(f"Unsupported model type: '{model_type}'.")

print("[Server Init] Initializing all required models...")
rag_handler = RAGHandler()
initialized_models: Dict[str, BaseLanguageModel] = {}
unique_model_configs = {}
for config_details in MODEL_CONFIGURATIONS.values():
    for model_key, model_info in config_details.items():
        if model_key != "templates":
            key_tuple = (model_info["type"], model_info.get("model_name"), model_info.get("base_url"), model_info.get("mode"))
            if key_tuple not in unique_model_configs:
                unique_model_configs[key_tuple] = model_info
for key_tuple, model_config in unique_model_configs.items():
    initialized_models[key_tuple] = get_model(model_config)
print(f"[Server Init] {len(initialized_models)} unique models loaded.")

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("[Server Lifespan] Preparing RAG pipeline...")
    rag_handler.setup_rag_pipeline()
    print("[Server Lifespan] RAG pipeline is ready.")
    yield
    print("[Server Lifespan] Application shutdown.")

app = FastAPI(title="Ultimate Hybrid Multi-LLM RAG API (Proxy Enabled)", lifespan=lifespan)

class MissionRequest(BaseModel):
    mission_query_zh: str
    selected_models: List[str]
class QueryRequest(BaseModel):
    user_input_zh: str
    phase1_analysis_map_en: Dict[str, str]
    summaries_map: Dict[str, str] = {}
    selected_models: List[str]
class SingleAnalysisResult(BaseModel):
    model_name: str
    analysis_result_zh: str
    analysis_result_en: str

async def _translate(text: str, template_obj: ChatPromptTemplate, llm_object: BaseLanguageModel):
    chain = template_obj | llm_object | StrOutputParser()
    return await chain.ainvoke({"text": text})

def get_model_from_config(model_info: Dict[str, Any]) -> BaseLanguageModel:
    key_tuple = (model_info["type"], model_info.get("model_name"), model_info.get("base_url"), model_info.get("mode"))
    return initialized_models[key_tuple]

@app.post("/analyze_mission_multi_stream")
async def analyze_mission_multi_stream_endpoint(request: MissionRequest):
    async def stream_generator() -> AsyncGenerator[str, None]:
        queue = asyncio.Queue()
        ANALYSIS_PIPELINE_STEPS = ["翻譯任務需求", "執行初步分析", "翻譯分析結果"]
        async def run_analysis(config_name: str, config_details: Dict):
            async def send_status(step_index, status, error_msg=None):
                await queue.put({"type": "status", "model_name": config_name, "step_index": step_index, "step_name": ANALYSIS_PIPELINE_STEPS[step_index], "status": status, "error": error_msg})
            mission_query_en = None
            try:
                analysis_model_config = config_details.get("analysis_model", config_details["rag_model"])
                analysis_llm = get_model_from_config(analysis_model_config)
                zh_to_en_model_obj = get_model_from_config(config_details["translator_zh_to_en"])
                en_to_zh_model_obj = get_model_from_config(config_details["translator_en_to_zh"])
                template_config = config_details["templates"]
                zh_to_en_template = TRANSLATION_PROMPT_TEMPLATES[template_config["zh_to_en"]]
                analysis_en_to_zh_template = TRANSLATION_PROMPT_TEMPLATES[template_config["analysis_en_to_zh"]]
                await send_status(0, "running")
                mission_query_en = await _translate(request.mission_query_zh, zh_to_en_template, zh_to_en_model_obj)
                await send_status(0, "complete")
                await send_status(1, "running")
                chain = MISSION_ANALYSIS_PROMPT | analysis_llm | StrOutputParser()
                analysis_en = await chain.ainvoke({"question": mission_query_en})
                await send_status(1, "complete")
                await send_status(2, "running")
                analysis_zh = await _translate(analysis_en, analysis_en_to_zh_template, en_to_zh_model_obj)
                await send_status(2, "complete")
                result = SingleAnalysisResult(model_name=config_name, analysis_result_zh=analysis_zh, analysis_result_en=analysis_en)
                await queue.put({"type": "full_response", "model_name": config_name, "content": result.model_dump()})
            except Exception as e:
                error_message = f"在處理 '{config_name}' 時發生嚴重錯誤: {str(e)}"
                print(error_message)
                await queue.put({"type": "error", "model_name": config_name, "content": error_message})
        tasks = [asyncio.create_task(run_analysis(name, MODEL_CONFIGURATIONS[name])) for name in request.selected_models if name in MODEL_CONFIGURATIONS]
        if tasks:
            finished_tasks_count = 0
            while finished_tasks_count < len(tasks):
                data = await queue.get()
                yield f"data: {json.dumps(data, ensure_ascii=False)}\n\n"
                if data.get("type") in ["full_response", "error"]:
                    finished_tasks_count += 1
        yield f"data: {json.dumps({'type': 'done'})}\n\n"
    return StreamingResponse(stream_generator(), media_type="text/event-stream")

@app.post("/query_components_multi_stream")
async def query_components_multi_stream_endpoint(request: QueryRequest):
    async def stream_generator() -> AsyncGenerator[str, None]:
        queue = asyncio.Queue()
        PIPELINE_STEPS = ["翻譯使用者問題", "分析查詢意圖", "檢索相關文件", "生成 RAG 回答", "翻譯最終結果", "更新對話摘要"]
        async def run_full_rag_and_summary_pipeline(config_name: str, config_details: Dict):
            async def send_status(step_index, status, error_msg=None):
                await queue.put({"type": "status", "model_name": config_name, "step_index": step_index, "step_name": PIPELINE_STEPS[step_index], "status": status, "error": error_msg})
            user_input_en = None
            try:
                rag_llm = get_model_from_config(config_details["rag_model"])
                zh_to_en_model_obj = get_model_from_config(config_details["translator_zh_to_en"])
                en_to_zh_model_obj = get_model_from_config(config_details["translator_en_to_zh"])
                template_config = config_details["templates"]
                mission_analysis_en = request.phase1_analysis_map_en.get(config_name, "...")
                previous_summary = request.summaries_map.get(config_name, "")
                zh_to_en_template = TRANSLATION_PROMPT_TEMPLATES[template_config["zh_to_en"]]
                rag_result_en_to_zh_template = TRANSLATION_PROMPT_TEMPLATES[template_config["rag_result_en_to_zh"]]
                await send_status(0, "running")
                user_input_en = await _translate(request.user_input_zh, zh_to_en_template, zh_to_en_model_obj)
                await send_status(0, "complete")
                await send_status(1, "running")
                analysis_parser = JsonOutputParser()
                analysis_chain = QUERY_ANALYSIS_PROMPT | rag_llm | analysis_parser
                search_keywords = user_input_en
                metadata_filter = None
                component_types = []
                try:
                    analysis_result = await asyncio.wait_for(analysis_chain.ainvoke({
                        "mission_summary": mission_analysis_en, 
                        "question": user_input_en, 
                        "category_list": "\n".join(f"- {c}" for c in rag_handler.component_types)
                    }), timeout=45.0)
                    search_keywords = analysis_result.get("keywords", user_input_en)
                    component_types = analysis_result.get("component_types", [])
                    if component_types:
                        metadata_filter = {"component_type": {"$in": component_types}}
                    await send_status(1, "complete")
                except Exception as e:
                    print(f"[{config_name}] Query analysis failed: {e}. Using original query.")
                    await send_status(1, "error", error_msg="意圖分析失敗，使用原始查詢")

                print(f"\n--- DEBUG: [{config_name}] ---")
                print(f"    - User Input (EN): {user_input_en}")
                print(f"    - Generated Keywords: {search_keywords}")
                print(f"    - Generated Component Types: {component_types}")
                
                await send_status(2, "running")
                # (*** 修改 ***) 呼叫您提供的 RAG 函式 retrieve_and_rank
                retrieved_docs = rag_handler.retrieve_and_rank(search_keywords, metadata_filter)
                
                print(f"    - Retrieved Docs Count: {len(retrieved_docs)}")
                print(f"--- END DEBUG ---\n")
                
                context = "\n\n---\n\n".join(doc.page_content for doc in retrieved_docs)
                sources = [doc.metadata for doc in retrieved_docs]
                await send_status(2, "complete")
                
                await send_status(3, "running")
                rag_chain = UNIFIED_RAG_PROMPT | rag_llm | StrOutputParser()
                response_en = await rag_chain.ainvoke({"question": user_input_en, "phase1_analysis_context": mission_analysis_en, "context": context, "chat_history": previous_summary})
                await send_status(3, "complete")
                
                await send_status(4, "running")
                response_zh = await _translate(response_en, rag_result_en_to_zh_template, en_to_zh_model_obj)
                await queue.put({"type": "full_response", "model_name": config_name, "content": {"response_zh": response_zh, "sources": sources}})
                await send_status(4, "complete")
                
                await send_status(5, "running")
                summary_chain = CONVERSATION_SUMMARY_PROMPT | rag_llm | StrOutputParser()
                new_summary = await summary_chain.ainvoke({"summary": previous_summary, "new_lines": f"Human: {user_input_en}\nAI: {response_en}"})
                await send_status(5, "complete")
                await queue.put({"type": "summary", "model_name": config_name, "content": new_summary.strip()})
            except Exception as e:
                error_message = f"在處理 '{config_name}' 時發生嚴重錯誤: {str(e)}"
                print(error_message)
                await queue.put({"type": "error", "model_name": config_name, "content": error_message})
        tasks = [asyncio.create_task(run_full_rag_and_summary_pipeline(name, MODEL_CONFIGURATIONS[name])) for name in request.selected_models if name in MODEL_CONFIGURATIONS]
        if tasks:
            finished_tasks_count = 0
            while finished_tasks_count < len(tasks):
                data = await queue.get()
                yield f"data: {json.dumps(data, ensure_ascii=False)}\n\n"
                if data.get("type") in ["summary", "error"]:
                    finished_tasks_count += 1
        yield f"data: {json.dumps({'type': 'done'})}\n\n"
    return StreamingResponse(stream_generator(), media_type="text/event-stream")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7777)
