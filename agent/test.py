from agents import set_tracing_export_api_key
from agents import Agent, Runner, function_tool
from typing import Optional
from transformers import AutoModelForCausalLM, AutoTokenizer
import asyncio
from huggingface_hub import login
import torch
import gradio as gr

# HuggingFace 登入
login(token="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")

# 設定 OpenAI Tracing（非必要可移除）
set_tracing_export_api_key('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')

# ==================== HuggingFace 模型 ====================
model_name = "taide/Llama-3.1-TAIDE-LX-8B-Chat"
tokenizer = AutoTokenizer.from_pretrained(model_name)
hf_model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)

# ==================== Tools ====================
@function_tool
def rag_tool(query: str) -> str:
    return f"[RAG] 查詢到的知識為：{query} 的背景資料..."

@function_tool
def simulation_tool(scenario: str) -> str:
    return f"[模擬] 情境 {scenario} 模擬完成。"

@function_tool
def formatter_tool(text: str, format: Optional[str] = "markdown") -> str:
    return f"[Formatter] 將文字轉換為 {format} 格式：{text}"

@function_tool
def llm_tool(prompt: str) -> str:
    return f"[LLM] 回覆：根據 {prompt} 推理結果為..."

@function_tool
def optimization_tool(result: str) -> str:
    return f"[優化] 已優化結果為：{result}"

tools_map = {
    "RAG 查詢": rag_tool,
    "情境模擬": simulation_tool,
    "格式化": formatter_tool,
    "LLM 推理": llm_tool,
    "結果優化": optimization_tool,
    "直接用模型": None
}

# ==================== 模型推論函式 ====================
def run_hf_model(prompt: str):
    inputs = tokenizer(prompt, return_tensors="pt").to(hf_model.device)
    outputs = hf_model.generate(**inputs, max_new_tokens=500, temperature=0.7, top_p=0.9)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# ==================== Gradio 互動邏輯 ====================
def process_input(user_input, selected_tool, format_type):
    if not user_input.strip():
        return "請輸入內容"

    # 如果選擇了工具，就用工具處理
    if tools_map[selected_tool] is not None:
        if selected_tool == "格式化":
            return tools_map[selected_tool](user_input, format_type)
        else:
            return tools_map[selected_tool](user_input)

    # 如果選擇 "直接用模型" → HuggingFace 推論
    return run_hf_model(user_input)

# ==================== Gradio 介面 ====================
with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Hoff 無人機專家 - 多功能 AI 工具")
    with gr.Row():
        with gr.Column(scale=2):
            user_input = gr.Textbox(lines=4, placeholder="輸入你的問題或內容...")
            selected_tool = gr.Dropdown(
                choices=list(tools_map.keys()),
                value="直接用模型",
                label="選擇工具"
            )
            format_type = gr.Dropdown(
                choices=["markdown", "html", "plaintext"],
                value="markdown",
                label="格式化輸出類型（僅在格式化工具時使用）"
            )
            submit_btn = gr.Button("送出")
        with gr.Column(scale=3):
            output_box = gr.Textbox(label="輸出結果", lines=10)

    submit_btn.click(
        fn=process_input,
        inputs=[user_input, selected_tool, format_type],
        outputs=output_box
    )

demo.launch(share=True)


