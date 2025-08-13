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

# ==================== 自訂 Hoff Agent ====================
class HoffAgent(Agent):
    async def respond(self, prompt: str) -> str:
        """改寫 Agent 直接用 HuggingFace 模型回應"""
        inputs = tokenizer(prompt, return_tensors="pt").to(hf_model.device)
        outputs = hf_model.generate(**inputs, max_new_tokens=500, temperature=0.7, top_p=0.9)
        return tokenizer.decode(outputs[0], skip_special_tokens=True)

hoff_agent = HoffAgent(
    name="Hoff",
    instructions="你是個無人機專家，並且你現在是個流程管理者，請依據使用者的提問協調工具完成任務。",
    tools=[rag_tool, simulation_tool, formatter_tool, llm_tool, optimization_tool],
    model="custom_hf"
)

# ==================== 主程式 ====================
async def main():
    prompt = "我需要一台可以長途飛行且可運輸大型物資的無人機，請問需要的動力規格與結構為何?"
    inputs = tokenizer(prompt, return_tensors="pt").to(hf_model.device)
    outputs = hf_model.generate(**inputs, max_new_tokens=500, temperature=0.7, top_p=0.9)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))
# ==================== Gradio 介面 ====================
def gradio_chat(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(hf_model.device)
    outputs = hf_model.generate(**inputs, max_new_tokens=500, temperature=0.7, top_p=0.9)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

iface = gr.Interface(
    fn=gradio_chat,
    inputs=gr.Textbox(lines=4, placeholder="輸入你的問題..."),
    outputs="text",
    title="Hoff 無人機專家",
    description="輸入需求，Hoff 將根據模型回答。"
)

if __name__ == "__main__":
    iface.launch()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
