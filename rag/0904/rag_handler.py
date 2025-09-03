# rag_handler.py

import os
import json
import logging
import hashlib
import uuid
import torch
import pickle
import shutil
from typing import List, Dict, Any, Optional

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain.retrievers import ParentDocumentRetriever
from langchain.storage import InMemoryStore
from langchain.text_splitter import RecursiveJsonSplitter, RecursiveCharacterTextSplitter
from sentence_transformers.cross_encoder import CrossEncoder

from config import (
    EMBEDDING_MODEL,
    CROSS_ENCODER_MODEL,
    DATA_PATH,
    VECTOR_STORE_PATH,
    DATA_HASH_PATH,
    PARENT_DOCS_CACHE_PATH,
    RETRIEVER_SEARCH_K,
    RERANKER_TOP_N
)
from models import DroneKnowledgeBase

# 設定日誌記錄
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RAGHandler:
    """
    負責處理所有與資料庫相關操作的類別，包括資料載入、
    向量化、儲存、檢索和重排。此類別不處理任何 LLM 相關邏輯。
    """
    def __init__(self):
        self.vectorstore: Optional[Chroma] = None
        self.docstore = InMemoryStore()
        self.embeddings: Optional[HuggingFaceEmbeddings] = None
        self.cross_encoder: Optional[CrossEncoder] = None
        self.component_types: List[str] = []
        self._initialize_core_components()

    def _initialize_core_components(self):
        """初始化 Embedding 模型和 Cross-Encoder 重排模型。"""
        try:
            device_to_use = 'cuda' if torch.cuda.is_available() else 'cpu'
            logging.info(f"Using device: {device_to_use}")

            logging.info(f"Initializing Embedding model: {EMBEDDING_MODEL}")
            self.embeddings = HuggingFaceEmbeddings(
                model_name=EMBEDDING_MODEL,
                model_kwargs={'device': device_to_use}
            )

            logging.info(f"Initializing Cross-Encoder re-ranker model: {CROSS_ENCODER_MODEL}")
            self.cross_encoder = CrossEncoder(CROSS_ENCODER_MODEL, device=device_to_use)
            
            logging.info("Core data components (Embeddings, Cross-Encoder) initialized.")
        except Exception as e:
            logging.error(f"Error during core component initialization: {e}", exc_info=True)
            raise

    def _calculate_data_hash(self) -> str:
        """計算 data_1 資料夾中所有 .json 檔案的 SHA256 hash 值。"""
        hasher = hashlib.sha256()
        if not os.path.isdir(DATA_PATH):
            logging.error(f"Data path '{DATA_PATH}' does not exist or is not a directory.")
            return ""
            
        files = sorted([f for f in os.listdir(DATA_PATH) if f.endswith(".json")])
        for filename in files:
            file_path = os.path.join(DATA_PATH, filename)
            try:
                with open(file_path, 'rb') as f:
                    while chunk := f.read(8192):
                        hasher.update(chunk)
            except IOError as e:
                logging.error(f"Could not read file {filename} for hashing: {e}")
                return ""
        return hasher.hexdigest()

    def _load_and_process_data(self) -> (List[Document], List[Document], List[str]):
        """從 JSON 檔案載入、驗證並處理資料，生成父文件和子文件塊。"""
        logging.info(f"Starting to load and process files from '{DATA_PATH}'...")
        all_parent_docs, all_child_docs, component_type_set = [], [], set()
        json_splitter = RecursiveJsonSplitter(max_chunk_size=500)

        for filename in os.listdir(DATA_PATH):
            if not filename.endswith(".json"):
                continue
            file_path = os.path.join(DATA_PATH, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    raw_data = json.load(f)
                
                validated_data = DroneKnowledgeBase.model_validate(raw_data)
                
                for main_key, main_module in validated_data:
                    if main_module is None: continue
                    for component_type_key, component_list in main_module:
                        if not component_list: continue
                        
                        component_type_set.add(component_type_key.lower())
                        for item in component_list:
                            item_dict = item.model_dump(mode='json', by_alias=True)
                            
                            doc_id = str(uuid.uuid4())
                            parent_content = json.dumps(item_dict, ensure_ascii=False)
                            
                            metadata = {
                                "doc_id": doc_id,
                                "source": filename,
                                "model_name": item_dict.get('model_name', 'N/A'),
                                "component_type": component_type_key.lower(),
                            }
                            all_parent_docs.append(Document(page_content=parent_content, metadata=metadata))

                            child_chunks = json_splitter.split_json(json_data=item_dict)
                            for chunk in child_chunks:
                                all_child_docs.append(Document(page_content=json.dumps(chunk, ensure_ascii=False), metadata={"doc_id": doc_id}))
            except Exception as e:
                logging.error(f"Error processing or validating file {filename}: {e}", exc_info=True)
        
        component_types = sorted(list(component_type_set))
        logging.info(f"File processing complete. Loaded {len(all_parent_docs)} parent docs, {len(all_child_docs)} child chunks.")
        logging.info(f"Detected component types: {component_types}")
        return all_parent_docs, all_child_docs, component_types

    def setup_rag_pipeline(self) -> bool:
        """
        建立或載入 RAG 管道。如果資料有變動或快取不存在，則重建資料庫。
        """
        try:
            current_hash = self._calculate_data_hash()
            if not current_hash: return False
            
            saved_hash = ""
            if os.path.exists(DATA_HASH_PATH):
                with open(DATA_HASH_PATH, 'r') as f:
                    saved_hash = json.load(f).get('hash', "")

            if current_hash == saved_hash and os.path.isdir(VECTOR_STORE_PATH) and os.path.exists(PARENT_DOCS_CACHE_PATH):
                logging.info("Data unchanged, loading from cache...")
                self.vectorstore = Chroma(persist_directory=VECTOR_STORE_PATH, embedding_function=self.embeddings)
                with open(PARENT_DOCS_CACHE_PATH, 'rb') as f:
                    parent_docs, self.component_types = pickle.load(f)
                self.docstore.mset([(doc.metadata["doc_id"], doc) for doc in parent_docs])
                logging.info(f"Loaded {len(parent_docs)} docs and {len(self.component_types)} types from cache.")
            else:
                logging.info("Data has changed or cache not found. Rebuilding RAG database...")
                if os.path.exists(VECTOR_STORE_PATH):
                    shutil.rmtree(VECTOR_STORE_PATH)
                parent_docs, child_docs, component_types = self._load_and_process_data()
                if not parent_docs or not child_docs:
                    logging.error("No documents were processed. Aborting database build.")
                    return False

                self.docstore.mset([(doc.metadata["doc_id"], doc) for doc in parent_docs])
                self.component_types = component_types
                
                os.makedirs(VECTOR_STORE_PATH, exist_ok=True)
                with open(PARENT_DOCS_CACHE_PATH, 'wb') as f:
                    pickle.dump((parent_docs, self.component_types), f)
                
                self.vectorstore = Chroma.from_documents(child_docs, self.embeddings, persist_directory=VECTOR_STORE_PATH)
                with open(DATA_HASH_PATH, 'w') as f:
                    json.dump({'hash': current_hash}, f)
                logging.info("Rebuild complete and cache saved.")
            
            return True if self.vectorstore else False
        except Exception as e:
            logging.error(f"Error building RAG pipeline: {e}", exc_info=True)
            return False

    def _retrieve_and_rerank(self, keywords: str) -> List[Document]:
        """
        執行檢索和重排的核心邏輯。
        
        Args:
            keywords (str): 用於檢索的英文查詢詞。
        
        Returns:
            List[Document]: 經過重排後，最相關的父文件列表。
        """
        if not self.vectorstore or not self.cross_encoder:
            logging.error("Vectorstore or Cross-Encoder not initialized. Cannot retrieve and rerank.")
            return []

        # 1. 向量檢索 (Retrieve)
        logging.info(f"Retrieving top {RETRIEVER_SEARCH_K} candidates for keywords: '{keywords[:50]}...'")
        retriever = ParentDocumentRetriever(
            vectorstore=self.vectorstore, 
            docstore=self.docstore,
            child_splitter=RecursiveCharacterTextSplitter(chunk_size=500), # 僅用於邏輯，實際已預先分割
            search_kwargs={"k": RETRIEVER_SEARCH_K}
        )
        retrieved_docs = retriever.invoke(keywords)
        if not retrieved_docs:
            logging.warning("No documents found after initial retrieval.")
            return []
        
        # 2. Cross-Encoder 重排 (Re-rank)
        logging.info(f"Re-ranking {len(retrieved_docs)} documents...")
        pairs = [[keywords, doc.page_content] for doc in retrieved_docs]
        scores = self.cross_encoder.predict(pairs)
        
        reranked_docs = [doc for _, doc in sorted(zip(scores, retrieved_docs), key=lambda x: x[0], reverse=True)]
        
        final_docs = reranked_docs[:RERANKER_TOP_N]
        logging.info(f"Re-ranking complete. Returning top {len(final_docs)} documents.")
        return final_docs
        
    def retrieve_and_rank(self, keywords: str, metadata_filter: Optional[Dict] = None) -> List[Document]:
        """
        公開的檢索與重排介面，供 API 伺服器呼叫。
        它會先執行核心的檢索與重排，然後再應用元數據過濾。
        """
        # 1. 呼叫內部的核心檢索與重排邏輯
        reranked_docs = self._retrieve_and_rerank(keywords)

        if not reranked_docs:
            return []

        # 2. 應用元數據過濾
        if metadata_filter and "component_type" in metadata_filter:
            allowed_types = metadata_filter["component_type"]["$in"]
            original_count = len(reranked_docs)
            
            final_docs = [
                doc for doc in reranked_docs 
                if doc.metadata.get("component_type") in allowed_types
            ]
            
            logging.info(f"Filtered final documents by metadata: {original_count} -> {len(final_docs)}")
            return final_docs
        
        return reranked_docs
