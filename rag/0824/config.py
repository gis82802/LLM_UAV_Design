# config.py

import os

# --- 路徑與基礎設定 ---
DATA_PATH = "./data_1"
VECTOR_STORE_PATH = "./chroma_db_store"
DATA_HASH_PATH = os.path.join(VECTOR_STORE_PATH, "data_hash.json")
PARENT_DOCS_CACHE_PATH = os.path.join(VECTOR_STORE_PATH, "parent_docs.pkl")
EMBEDDING_MODEL = "BAAI/bge-m3"
CROSS_ENCODER_MODEL = 'cross-encoder/ms-marco-MiniLM-L-6-v2'

# --- RAG 檢索設定 ---
RETRIEVER_SEARCH_K = 20
RERANKER_TOP_N = 10

# --- Ollama 伺服器設定 ---
OLLAMA_BASE_URL = "http://192.168.2.100:8001"

# ===================================================================
# --- ✨ Ollama 模型組合設定區 ✨ ---
#
# 新增 "analysis_model"，專門用於第一階段的初步分析。
# 為不同任務 (翻譯、分析、RAG) 設定了最佳化的 Ollama 參數。
# ===================================================================

MODEL_CONFIGURATIONS = {
    "Llama3.3-70B q8 (全任務)": {
        
        "rag_model": {
            "type": "ollama", "model_name": "llama3.3:70b-instruct-q8_0", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": {
                "temperature": 0.2,       
                "top_k": 40,
                "num_ctx": 16384
            }
        },
   
        "analysis_model": {
            "type": "ollama", "model_name": "llama3.3:70b-instruct-q8_0", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": {
                "temperature": 0.3,        
                "top_k": 40,
                "num_ctx": 16384
            }
        },
 
        "translator_zh_to_en": {
            "type": "ollama", "model_name": "llama3.3:70b-instruct-q8_0", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": { "temperature": 0.2, "top_k": 40 }
        },
        "translator_en_to_zh": {
            "type": "ollama", "model_name": "llama3.3:70b-instruct-q8_0", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": { "temperature": 0.2, "top_k": 40 }
        },
        "templates": { "zh_to_en": "ZH_TO_EN_SIMPLE_EN", "analysis_en_to_zh": "ANALYSIS_EN_TO_ZH_DETAILED_EN", "rag_result_en_to_zh": "RAG_RESULT_EN_TO_ZH_DETAILED_EN" }
    },

    "gpt-oss-120b (全任務)": {
        "rag_model": {
            "type": "ollama", "model_name": "gpt-oss:120b", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": { "temperature": 0.2, "top_k": 40,"num_ctx": 16384 }
        },
        "analysis_model": {
            "type": "ollama", "model_name": "gpt-oss:120b", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": { "temperature": 0.3, "top_k": 40, "num_ctx": 16384 }
        },
        "translator_zh_to_en": {
            "type": "ollama", "model_name": "gpt-oss:120b", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": { "temperature": 0.2, "top_k": 40 }
        },
        "translator_en_to_zh": {
            "type": "ollama", "model_name": "gpt-oss:120b", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": { "temperature": 0.2, "top_k": 40 }
        },
        "templates": { "zh_to_en": "ZH_TO_EN_SIMPLE_EN", "analysis_en_to_zh": "ANALYSIS_EN_TO_ZH_DETAILED_EN", "rag_result_en_to_zh": "RAG_RESULT_EN_TO_ZH_DETAILED_EN" }
    },

    "TAIDE(中翻英) + Llama3-70B(核心)": {
        "rag_model": {
            "type": "ollama", "model_name": "llama3.3:70b-instruct-q8_0", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": { "temperature": 0.2, "top_k": 40,  "num_ctx": 16384 }
        },
        "analysis_model": {
            "type": "ollama", "model_name": "llama3.3:70b-instruct-q8_0", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": { "temperature": 0.3, "top_k": 40, "num_ctx": 16384 }
        },
   
        "translator_zh_to_en": {
            "type": "ollama", "model_name": "Yu-Feng/Llama-3.1-TAIDE-LX-8B-Chat:FP16", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": { "temperature": 0.2, "top_k": 40 }
        },
        "translator_en_to_zh": { 
            "type": "ollama", "model_name": "llama3.3:70b-instruct-q8_0", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": { "temperature": 0.2, "top_k": 40 }
        },
        "templates": { "zh_to_en": "ZH_TO_EN_SIMPLE_ZH", "analysis_en_to_zh": "ANALYSIS_EN_TO_ZH_DETAILED_ZH", "rag_result_en_to_zh": "RAG_RESULT_EN_TO_ZH_DETAILED_ZH" }
    },
    
    "GPT-5-mini": {
        "rag_model": { "type": "proxy", "base_url": "https://api.chatanywhere.org/v1", "api_key_env": "CHATANYWHERE_API_KEY", "model_name": "gpt-5-mini-ca" },
        "analysis_model": { "type": "proxy", "base_url": "https://api.chatanywhere.org/v1", "api_key_env": "CHATANYWHERE_API_KEY", "model_name": "gpt-5-mini-ca" },
        "translator_zh_to_en": { "type": "proxy", "base_url": "https://api.chatanywhere.tech/v1", "api_key_env": "CHATANYWHERE_API_KEY", "model_name": "gpt-5-mini-ca" },
        "translator_en_to_zh": { "type": "proxy", "base_url": "https://api.chatanywhere.tech/v1", "api_key_env": "CHATANYWHERE_API_KEY", "model_name": "gpt-5-mini-ca" },
        "templates": { "zh_to_en": "ZH_TO_EN_SIMPLE_EN", "analysis_en_to_zh": "ANALYSIS_EN_TO_ZH_DETAILED_EN", "rag_result_en_to_zh": "RAG_RESULT_EN_TO_ZH_DETAILED_ZH" }
    },

    "TAIDE(雙向翻譯) + Llama3-70B(核心)": {
        "rag_model": {
            "type": "ollama", "model_name": "llama3.3:70b-instruct-q8_0", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": { "temperature": 0.2, "top_k": 40, "num_ctx": 16384 }
        },
        "analysis_model": {
            "type": "ollama", "model_name": "llama3.3:70b-instruct-q8_0", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": { "temperature": 0.2, "top_k": 40, "num_ctx": 16384 }
        },
        "translator_zh_to_en": {
            "type": "ollama", "model_name": "Yu-Feng/Llama-3.1-TAIDE-LX-8B-Chat:FP16", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": { "temperature": 0.2, "top_k": 40 }
        },
        "translator_en_to_zh": {
            "type": "ollama", "model_name": "Yu-Feng/Llama-3.1-TAIDE-LX-8B-Chat:FP16", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": { "temperature": 0.2, "top_k": 40}
        },
        "templates": { "zh_to_en": "ZH_TO_EN_SIMPLE_ZH", "analysis_en_to_zh": "ANALYSIS_EN_TO_ZH_DETAILED_ZH", "rag_result_en_to_zh": "RAG_RESULT_EN_TO_ZH_DETAILED_EN" }
    },
    "TAIDE(雙向翻譯) + gpt oss 120b(核心)": {
        "rag_model": {
            "type": "ollama", "model_name": "gpt-oss:120b", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": { "temperature": 0.2,  "num_ctx": 16384 }
        },
        "analysis_model": {
            "type": "ollama", "model_name": "gpt-oss:120b", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": { "temperature": 0.3, "top_k": 40, "num_ctx": 16384 }
        },

        "translator_zh_to_en": {
            "type": "ollama", "model_name": "Yu-Feng/Llama-3.1-TAIDE-LX-8B-Chat:FP16", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": { "temperature": 0.2, "top_k": 40 }
        },
        "translator_en_to_zh": {
            "type": "ollama", "model_name": "Yu-Feng/Llama-3.1-TAIDE-LX-8B-Chat:FP16", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": { "temperature": 0.2, "top_k": 40 }
        },
        "templates": { "zh_to_en": "ZH_TO_EN_SIMPLE_ZH", "analysis_en_to_zh": "ANALYSIS_EN_TO_ZH_DETAILED_ZH", "rag_result_en_to_zh": "RAG_RESULT_EN_TO_ZH_DETAILED_ZH" }
    }
}
