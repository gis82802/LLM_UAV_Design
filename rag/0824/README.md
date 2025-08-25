# AI 無人機設計協作平台

本專案是一個基於多大型語言模型 (Multi-LLM) 的混合式 RAG (Retrieval-Augmented Generation) 系統，旨在協助無人機設計工程師根據任務需求，快速查詢、分析和選擇合適的硬體元件。系統前端使用 Gradio 搭建，後端由 FastAPI 提供 API 服務。

## 核心功能

  - **混合式多模型架構**: 支援同時使用多個本地 Ollama 模型和遠端類 OpenAI API (Proxy) 進行查詢，並可在前端介面比較不同模型組合的回答品質。
  - **進階 RAG 管道**:
      - **父文件檢索 (Parent Document Retriever)**: 處理大型元件規格文件，確保檢索到的上下文完整。
      - **交叉編碼器重排 (Cross-Encoder Reranking)**: 在初步檢索後，使用 Cross-Encoder 模型對結果進行精準排序，提升回答的相關性。
  - **兩階段式對話流程**:
    1.  **任務分析 (Mission Analysis)**: 使用者首先輸入高階任務需求，LLM 會進行初步分析，生成各模組的設計考量。
    2.  **元件查詢 (Component Query)**: 在任務分析的基礎上，使用者可以進一步提出具體問題，RAG 系統會從知識庫中檢索並推薦相關元件。
  - **即時串流響應**: 後端和前端皆採用 Server-Sent Events (SSE) 進行串流通信，即時顯示 LLM 的處理進度和最終結果，提升使用者體驗。
  - **動態意圖分析**: 在第二階段查詢中，LLM 會先分析使用者問題，提取關鍵字和元件類型，以縮小檢索範圍，提升 RAG 的精準度。

## 系統架構

本系統由前端 UI 和後端 API 伺服器組成，兩者獨立運行。

```mermaid
graph TD
    subgraph "使用者端"
        A[使用者 Browser]
    end

    subgraph "前端服務 (Gradio)"
        B[Gradio UI - gradio_ui_chatbot.py]
    end

    subgraph "後端服務 (FastAPI)"
        C[API Server - api_server_multi_llm.py]
        D[RAG 核心 - rag_handler.py]
        E[向量資料庫 - ChromaDB]
        F[文件知識庫 - data_1/*.json]
    end

    subgraph "LLM 服務 (遠端)"
        G[Ollama Server @ 192.168.2.100:8001]
        H[Proxy API (e.g., ChatAnywhere)]
    end

    A -- HTTP --> B
    B -- API Requests --> C
    C -- 執行 RAG --> D
    D -- 讀取資料 --> F
    D -- 嵌入/檢索 --> E
    C -- LLM 推理 --> G
    C -- LLM 推理 --> H
```

## 專案結構

```
.
├── data_1/                     # 原始資料來源
│   ├── power.json
│   ├── sensor.json
│   └── structure.json
├── chroma_db_store/            # ChromaDB 向量儲存目錄 (自動生成)
├── api_server_multi_llm.py     # 後端 FastAPI 伺服器
├── gradio_ui_chatbot.py        # 前端 Gradio 應用程式
├── rag_handler.py              # RAG 核心邏輯 (載入、嵌入、檢索、重排)
├── config.py                   # 專案核心設定 (模型組合、RAG 參數)
├── prompts.py                  # 所有 LangChain 提示詞
├── models.py                   # Pydantic 資料模型，用於驗證 JSON 資料
├── requirements.txt            # Python 依賴套件
├── .env.example                # 環境變數範本檔
└── README.md                   # 本文件
```

## 環境設置與安裝

#### 1\. 先決條件

  - Python 3.9 或更高版本
  - Git
  - 確保您的開發機能夠訪問團隊共用的 Ollama 伺服器，地址為 `192.168.2.100:8001`。**您不需要在本機自行啟動 Ollama。**

#### 2\. 安裝步驟

1.  **克隆專案**

    ```bash
    git clone <your-repository-url>
    cd <repository-name>
    ```

2.  **建立並啟用虛擬環境**

    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **安裝依賴套件**

    ```bash
    pip install -r requirements.txt
    ```

    *注意: `torch` 的安裝可能會因為您的 CUDA 版本而異。如果 `requirements.txt` 中的版本不適用，請參考 [PyTorch 官網](https://pytorch.org/) 的指引進行安裝。*

4.  **設定環境變數**
    專案使用 `.env` 文件來管理 API 金鑰。請將 `.env.example` 複製為 `.env`，並填入必要的金鑰。

    ```bash
    cp .env.example .env
    ```

    接著編輯 `.env` 文件：

    ```dotenv
    # .env
    # 用於 OpenAI 相容 API 的金鑰 (例如 ChatAnywhere)
    CHATANYWHERE_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxx"
    ```

5.  **確認資料檔案**
    請確保 `power.json`, `sensor.json`, `structure.json` 三個知識庫檔案已放置在 `data_1` 資料夾中。

## 如何運行

您需要開啟兩個終端機視窗，分別啟動後端 API 伺服器和前端 Gradio 介面。

#### 1\. 啟動後端 API 伺服器

在第一個終端機中，直接執行 `api_server_multi_llm.py` 檔案：

```bash
python api_server_multi_llm.py
```

該腳本將會啟動一個 Uvicorn 伺服器，監聽 `0.0.0.0:7777`。

#### 2\. 啟動前端 Gradio UI

在第二個終端機中，運行以下命令：

```bash
python gradio_ui_chatbot.py
```

Gradio 服務預設會運行在 `http://127.0.0.1:7860`。請在瀏覽器中開啟此地址即可開始使用。

> **⚠️ 注意：關於端口佔用**
>
>   - 後端 API 預設使用 **7777** 端口，前端 UI 預設使用 **7860** 端口。
>   - 如果啟動時提示端口已被佔用 (Port is already in use)，請手動修改對應檔案中的端口號。
>       - **後端**: 修改 `api_server_multi_llm.py` 文件底部的 `uvicorn.run(app, host="0.0.0.0", port=7777)`。
>       - **前端**: 修改 `gradio_ui_chatbot.py` 文件底部的 `demo.queue().launch(server_name="0.0.0.0", server_port=7860)`。

## API 端點

後端服務提供以下主要的 API 端點供前端調用：

  - **`POST /analyze_mission_multi_stream`**

      - **功能**: 執行第一階段的任務分析。
      - **Request Body**:
        ```json
        {
          "mission_query_zh": "您的任務描述",
          "selected_models": ["模型組合名稱1", "模型組合名稱2"]
        }
        ```
      - **Response**: `text/event-stream` 格式的串流響應。

  - **`POST /query_components_multi_stream`**

      - **功能**: 執行第二階段的元件查詢和 RAG。
      - **Request Body**:
        ```json
        {
          "user_input_zh": "您的具體問題",
          "phase1_analysis_map_en": { "模型組合名稱1": "第一階段的英文分析結果" },
          "summaries_map": { "模型組合名稱1": "先前的對話摘要" },
          "selected_models": ["模型組合名稱1", "模型組合名稱2"]
        }
        ```
      - **Response**: `text/event-stream` 格式的串流響應。

## 模型與 RAG 設定

所有關於模型組合和 RAG 管道的設定都集中在 `config.py` 檔案中，方便團隊成員進行調整和實驗。

  - **`MODEL_CONFIGURATIONS`**:

      - 在此字典中可以定義新的模型組合或修改現有組合。
      - 每個組合可以為 `rag_model`, `analysis_model`, `translator_zh_to_en`, `translator_en_to_zh` 等不同角色指定不同的 LLM。
      - 支援 `ollama` 和 `proxy` 兩種模型類型。
      - 可以為 Ollama 模型設定 `temperature`, `top_k`, `num_ctx` 等參數。

  - **RAG 檢索設定**:

      - `RETRIEVER_SEARCH_K`: 初步檢索時返回的文件數量。
      - `RERANKER_TOP_N`: 經過 Cross-Encoder 重排後，最終提供給 LLM 的文件數量。

  - **嵌入與重排模型**:

      - `EMBEDDING_MODEL`: 用於文件嵌入的句子轉換器模型。
      - `CROSS_ENCODER_MODEL`: 用於結果重排的 Cross-Encoder 模型。