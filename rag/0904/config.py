import os

# --- PATHS AND BASIC SETTINGS ---
DATA_PATH = "./data_1"
VECTOR_STORE_PATH = "./chroma_db_store"
DATA_HASH_PATH = os.path.join(VECTOR_STORE_PATH, "data_hash.json")
PARENT_DOCS_CACHE_PATH = os.path.join(VECTOR_STORE_PATH, "parent_docs.pkl")
EMBEDDING_MODEL = "BAAI/bge-m3"
CROSS_ENCODER_MODEL = 'cross-encoder/ms-marco-MiniLM-L-6-v2'

# --- RAG RETRIEVAL SETTINGS ---
RETRIEVER_SEARCH_K = 30
RERANKER_TOP_N = 20

# --- OLLAMA SERVER SETTINGS ---
OLLAMA_BASE_URL = "http://192.168.2.100:8001"

# ===================================================================
# --- ✨ Ollama Model Combination Settings ✨ ---
#
# "analysis_model" is specialized for the initial analysis in the first stage.
# Optimized Ollama parameters are set for different tasks (translation, analysis, RAG).
# ===================================================================

MODEL_CONFIGURATIONS = {
    "Llama3.3-70B q8 (All Tasks)": {
        "rag_model": {
            "type": "ollama", "model_name": "llama3.3:70b-instruct-q8_0", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": {
                "temperature": 0.8,     # 已修改
                "top_k": 20,           
                "num_ctx": 16384
            }
        },
        "analysis_model": {
            "type": "ollama", "model_name": "llama3.3:70b-instruct-q8_0", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": {
                "temperature": 0.8,     # 已修改
                "top_k": 30,           
                "num_ctx": 16384
            }
        },
        "translator_zh_to_en": {
            "type": "ollama", "model_name": "llama3.3:70b-instruct-q8_0", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": { "temperature": 0.8, "top_k": 40 } # 已修改
        },
        "translator_en_to_zh": {
            "type": "ollama", "model_name": "llama3.3:70b-instruct-q8_0", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": { "temperature": 0.8, "top_k": 40 } # 已修改
        },
        "templates": { "zh_to_en": "ZH_TO_EN_SIMPLE_EN", "analysis_en_to_zh": "ANALYSIS_EN_TO_ZH_DETAILED_EN", "rag_result_en_to_zh": "RAG_RESULT_EN_TO_ZH_DETAILED_EN" }
    },

    "gpt-oss-120b (All Tasks)": {
        "rag_model": {
            "type": "ollama", "model_name": "gpt-oss:120b", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": {
                "temperature": 0.8,     # 已修改
                "top_k": 20,           
                "num_ctx": 16384
            }
        },
        "analysis_model": {
            "type": "ollama", "model_name": "gpt-oss:120b", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": {
                "temperature": 0.8,     # 已修改
                "top_k": 30,           
                "num_ctx": 16384
            }
        },
        "translator_zh_to_en": {
            "type": "ollama", "model_name": "gpt-oss:120b", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": { "temperature": 0.8, "top_k": 40 } # 已修改
        },
        "translator_en_to_zh": {
            "type": "ollama", "model_name": "gpt-oss:120b", "mode": "chat", "base_url": OLLAMA_BASE_URL,
            "options": { "temperature": 0.8, "top_k": 40 } # 已修改
        },
        "templates": { "zh_to_en": "ZH_TO_EN_SIMPLE_EN", "analysis_en_to_zh": "ANALYSIS_EN_TO_ZH_DETAILED_EN", "rag_result_en_to_zh": "RAG_RESULT_EN_TO_ZH_DETAILED_EN" }
    },

    "GPT-5-mini": {
        "rag_model": { "type": "proxy", "base_url": "https://api.chatanywhere.org/v1", "api_key_env": "CHATANYWHERE_API_KEY", "model_name": "gpt-5-mini-ca" },
        "analysis_model": { "type": "proxy", "base_url": "https://api.chatanywhere.org/v1", "api_key_env": "CHATANYWHERE_API_KEY", "model_name": "gpt-5-mini-ca" },
        "translator_zh_to_en": { "type": "proxy", "base_url": "https://api.chatanywhere.tech/v1", "api_key_env": "CHATANYWHERE_API_KEY", "model_name": "gpt-5-mini-ca" },
        "translator_en_to_zh": { "type": "proxy", "base_url": "https://api.chatanywhere.tech/v1", "api_key_env": "CHATANYWHERE_API_KEY", "model_name": "gpt-5-mini-ca" },
        "templates": { "zh_to_en": "ZH_TO_EN_SIMPLE_EN", "analysis_en_to_zh": "ANALYSIS_EN_TO_ZH_DETAILED_EN", "rag_result_en_to_zh": "RAG_RESULT_EN_TO_ZH_DETAILED_ZH" }
    },

    'gemini-2.5-flash': {
        "analysis_model": {
            "type": "google_genai",
            "model_name": "gemini-2.5-flash",
            "reasoning_effort": "high"
        },
        "rag_model": {
            "type": "google_genai",
            "model_name": "gemini-2.5-flash",
            "reasoning_effort": "high"
        },
        "translator_zh_to_en": {
            "type": "google_genai",
            "model_name": "gemini-2.5-flash"
        },
        "translator_en_to_zh": {
            "type": "google_genai",
            "model_name": "gemini-2.5-flash"
        },
        "templates": {
            "zh_to_en": "ZH_TO_EN_SIMPLE_EN",
            "analysis_en_to_zh": "ANALYSIS_EN_TO_ZH_DETAILED_EN",
            "rag_result_en_to_zh": "RAG_RESULT_EN_TO_ZH_DETAILED_EN"
        }
    },
    'gemini-2.5-flash（翻譯）+ gemini-2.5-pro(核心)': {
        "analysis_model": {
            "type": "google_genai",
            "model_name": "gemini-2.5-pro",
            "reasoning_effort": "high"
        },
        "rag_model": {
            "type": "google_genai",
            "model_name": "gemini-2.5-pro",
            "reasoning_effort": "high"
        },
        "translator_zh_to_en": {
            "type": "google_genai",
            "model_name": "gemini-2.5-flash"
        },
        "translator_en_to_zh": {
            "type": "google_genai",
            "model_name": "gemini-2.5-flash"
        },
        "templates": {
            "zh_to_en": "ZH_TO_EN_SIMPLE_EN",
            "analysis_en_to_zh": "ANALYSIS_EN_TO_ZH_DETAILED_EN",
            "rag_result_en_to_zh": "RAG_RESULT_EN_TO_ZH_DETAILED_EN"
        }
    }
}
