# rag_handler.py

import os
import json
import logging
import hashlib
import uuid
import torch
from typing import List, Dict, Any, Optional

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain.storage import InMemoryStore
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.retrievers import ParentDocumentRetriever
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_transformers import LongContextReorder
from sentence_transformers import CrossEncoder

from config import (
    EMBEDDING_MODEL,
    CROSS_ENCODER_MODEL,
    DATA_PATH,
    VECTOR_STORE_PATH,
    DATA_HASH_PATH,
    PARENT_DOCS_CACHE_PATH,
    RERANKER_TOP_N
)
from models import DroneKnowledgeBase

# 設定日誌記錄
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RAGHandler:
    def __init__(self):
        self.vectorstore: Optional[Chroma] = None
        self.docstore = InMemoryStore()
        self.embeddings: Optional[HuggingFaceEmbeddings] = None
        self.cross_encoder: Optional[CrossEncoder] = None
        self.retriever: Optional[ParentDocumentRetriever] = None
        self.component_types: List[str] = []
        self._initialize_models()

    def _initialize_models(self):
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
            
            logging.info("Core data models (Embeddings, Cross-Encoder) initialized.")
        except Exception as e:
            logging.error(f"Error during model initialization: {e}", exc_info=True)
            raise

    def setup_rag_pipeline(self):
        logging.info("Setting up RAG pipeline...")
        # 這裡可以加入檢查資料 hash 的邏輯來決定是否需要重建
        # 為簡化，此處我們總是重建或載入
        
        # 載入資料並建立檢索器
        parent_docs, child_docs, component_types = self._load_and_process_data()
        self.component_types = component_types

        # 使用 Chroma 作為向量儲存
        self.vectorstore = Chroma(
            collection_name="split_parents",
            embedding_function=self.embeddings
        )
        
        # 建立 ParentDocumentRetriever
        self.retriever = ParentDocumentRetriever(
            vectorstore=self.vectorstore,
            docstore=self.docstore,
            child_splitter=RecursiveCharacterTextSplitter(chunk_size=400),
            parent_splitter=RecursiveCharacterTextSplitter(chunk_size=2000),
        )
        self.retriever.add_documents(parent_docs, ids=None, add_to_docstore=True)
        logging.info("ParentDocumentRetriever setup complete.")

    def _load_and_process_data(self) -> (List[Document], List[Document], List[str]):
        logging.info(f"Loading files from '{DATA_PATH}'...")
        all_parent_docs, all_child_docs, component_type_set = [], [], set()
        child_splitter = RecursiveCharacterTextSplitter(chunk_size=400)

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
                            content = json.dumps(item_dict, ensure_ascii=False)
                            metadata = {
                                "source": filename,
                                "model_name": item_dict.get('model_name', 'N/A'),
                                "component_type": component_type_key.lower(),
                            }
                            doc = Document(page_content=content, metadata=metadata)
                            all_parent_docs.append(doc)
            except Exception as e:
                logging.error(f"Error processing file {filename}: {e}", exc_info=True)
        
        component_types = sorted(list(component_type_set))
        logging.info(f"Loaded {len(all_parent_docs)} documents.")
        logging.info(f"Detected component types: {component_types}")
        return all_parent_docs, [], component_types

    def retrieve_and_rank(self, query: str, metadata_filter: Optional[Dict] = None) -> List[Document]:
        logging.info(f"Starting retrieval and ranking for query: '{query[:50]}...'")
        if not self.retriever or not self.cross_encoder:
            logging.error("Retriever or Cross-Encoder not initialized.")
            return []

        # 1. 使用 ParentDocumentRetriever 檢索
        retrieved_docs = self.retriever.get_relevant_documents(query)

        # 手動應用元數據過濾 (如果需要)
        if metadata_filter and "component_type" in metadata_filter:
            allowed_types = metadata_filter["component_type"]["$in"]
            retrieved_docs = [
                doc for doc in retrieved_docs 
                if doc.metadata.get("component_type") in allowed_types
            ]

        if not retrieved_docs:
            logging.warning("No documents retrieved after initial search and filtering.")
            return []
        
        logging.info(f"Retrieved {len(retrieved_docs)} documents for re-ranking.")

        # 2. Cross-Encoder 重排
        pairs = [[query, doc.page_content] for doc in retrieved_docs]
        scores = self.cross_encoder.predict(pairs)
        
        reranked_docs = [doc for _, doc in sorted(zip(scores, retrieved_docs), key=lambda x: x[0], reverse=True)]
        
        # 3. LongContextReorder 將最相關的文件放在開頭和結尾
        reordering = LongContextReorder()
        reordered_docs = reordering.transform_documents(reranked_docs)

        final_docs = reordered_docs[:RERANKER_TOP_N]
        logging.info(f"Re-ranking and reordering complete. Returning top {len(final_docs)} documents.")
        
        return final_docs
