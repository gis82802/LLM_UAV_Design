# gradio_ui_chatbot.py

import gradio as gr
import requests
import json
import re
from config import MODEL_CONFIGURATIONS

# --- 基礎設定 ---
API_URL = "http://127.0.0.1:7777"
MODEL_CONFIG_ORDER = list(MODEL_CONFIGURATIONS.keys())

# --- 流程步驟定義 ---
ANALYSIS_PIPELINE_STEPS = ["翻譯任務需求", "執行初步分析", "翻譯分析結果"]
QUERY_PIPELINE_STEPS = ["翻譯使用者問題", "分析查詢意圖", "檢索相關文件", "生成 RAG 回答", "翻譯最終結果", "更新對話摘要"]

# --- 自訂 CSS ---
CUSTOM_CSS = """
body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
#title_md { text-align: center; color: #333; }
.gradio-container { max-width: 1280px !important; margin: auto !important; }
#main-col { gap: 20px; }
#status-display-wrapper { padding: 12px; border: 1px solid #e0e0e0; border-radius: 8px; background-color: #f9f9f9; }
.gr-tab-item { flex-grow: 1; text-align: center; }
#welcome-screen { text-align: center; padding: 40px; }
"""

# --- 格式化與輔助函式 ---
def format_single_analysis_response(result: dict) -> str:
    if not result: return "❌ 模型分析失敗，請檢查後端日誌。"
    model_name = result.get('model_name', '未知模型')
    analysis = result.get('analysis_result_zh', '無結果')
    return f"### 🧠 **模型: {model_name}**\n{analysis}\n\n"

def format_single_query_response(data: dict) -> str:
    formatted_text = ""
    if data.get("error"):
        return f"❌ **執行時發生錯誤:**\n`{data['error']}`\n\n"
    response_zh = data.get("response_zh", "模型未提供中文回應。")
    sources = data.get("sources", [])
    formatted_text += f"{response_zh}\n\n"
    if sources:
        formatted_text += "#### 📄 **參考資料來源**\n"
        unique_sources = list({s.get('model_name', 'N/A'): s for s in sources}.values())
        for i, source in enumerate(unique_sources[:5]):
            model_name_src = source.get('model_name', 'N/A')
            component_type = source.get('component_type', 'N/A')
            file_source = source.get('source', 'N/A')
            formatted_text += f"- **元件:** `{model_name_src}` (類型: {component_type}, 檔案: {file_source})\n"
        if len(unique_sources) > 5:
            formatted_text += f"- ... 以及其他 {len(unique_sources) - 5} 個來源。\n"
    return formatted_text

def create_status_markdown(selected_models, steps: list):
    if not selected_models: return ""
    md = "### 🚀 執行狀態\n"
    for model_name in selected_models:
        safe_model_name = re.sub(r'[^a-zA-Z0-9]', '-', model_name)
        md += f"<div id='status-{safe_model_name}'><p><strong>{model_name}</strong></p>"
        for i, step in enumerate(steps):
            md += f"<p id='step-{safe_model_name}-{i}' style='margin: 2px 0 2px 20px;'>⚪ {step}</p>"
        md += "</div>\n"
    return md

def update_status_markdown(current_md: str, event: dict, steps: list) -> str:
    model_name, step_index, status, error_msg = event.get("model_name"), event.get("step_index"), event.get("status"), event.get("error")
    if model_name is None or step_index is None or status is None: return current_md
    icon, color = {"running": ("⏳", "orange"), "complete": ("✅", "green"), "error": ("❌", "red")}.get(status, ("⚪", "black"))
    step_name = steps[step_index]
    safe_model_name = re.sub(r'[^a-zA-Z0-9]', '-', model_name)
    new_line = f"<p id='step-{safe_model_name}-{step_index}' style='margin: 2px 0 2px 20px; color: {color};'>{icon} {step_name}"
    if error_msg: new_line += f" ({error_msg})"
    new_line += "</p>"
    pattern = re.compile(f"<p id='step-{safe_model_name}-{step_index}'.*?>.*?</p>")
    return pattern.sub(new_line, current_md) if pattern.search(current_md) else current_md


# --- Gradio 介面佈局 ---
with gr.Blocks(theme=gr.themes.Soft(), css=CUSTOM_CSS, title="AI 無人機設計平台") as demo:
    # 狀態管理
    phase_state = gr.State("ANALYSIS_PENDING")
    phase1_analysis_map_state = gr.State({})
    summaries_map_state = gr.State({})
    chat_histories_state = gr.State({model_name: [] for model_name in MODEL_CONFIG_ORDER})

    with gr.Row(elem_id="main-col"):
        with gr.Column(scale=3):
            gr.Markdown("# AI 無人機設計協作平台", elem_id="title_md")
            
            with gr.Group(visible=True, elem_id="welcome-screen") as welcome_screen:
                gr.Markdown("## 歡迎使用 AI 無人機設計協作平台")
                gr.Markdown("請在右側選擇您想諮詢的模型組合，然後在下方的輸入框中描述您的任務需求。")

            with gr.Group(visible=False) as chat_interface_wrapper:
                chatbots = {}
                with gr.Tabs(elem_id="output_tabs") as output_tabs:
                    for model_name in MODEL_CONFIG_ORDER:
                        with gr.Tab(model_name, id=model_name):
                            chatbots[model_name] = gr.Chatbot(
                                label=f"對話紀錄 ({model_name})",
                                height=680,
                                type='messages',
                                elem_id=f"chatbot_{re.sub(r'[^a-zA-Z0-9]', '_', model_name)}",
                                show_copy_button=True
                            )

            with gr.Row(elem_id="input-row"):
                msg_input = gr.Textbox(placeholder="請在此輸入任務需求或查詢問題...", scale=9, container=False, elem_id="msg-input")
                send_btn = gr.Button("送出", variant="primary", min_width=100)

        with gr.Column(scale=1):
            with gr.Group():
                gr.Markdown("### ⚙️ 模型執行選項")
                model_checkboxes = gr.CheckboxGroup(choices=MODEL_CONFIG_ORDER, label="選擇要執行的模型組合", value=[MODEL_CONFIG_ORDER[0]] if MODEL_CONFIG_ORDER else [])
            with gr.Group(elem_id="status-display-wrapper"):
                status_display = gr.Markdown(visible=False)
            clear_btn = gr.Button("🗑️ 清除對話紀錄", variant="stop")

    # --- 核心事件處理邏輯 ---
    def handle_submit(user_message: str, selected_models: list, current_phase: str, histories: dict, phase1_map: dict, summaries_map: dict):
        if not user_message.strip():
            gr.Warning("輸入不能為空！")
            yield {msg_input: gr.update(value=user_message)}
            return
        if not selected_models:
            gr.Warning("請至少選擇一個模型組合！")
            yield {}
            return
        
        updates = {msg_input: gr.update(value="", interactive=False)}
        if current_phase == "ANALYSIS_PENDING":
            updates[welcome_screen] = gr.update(visible=False)
            updates[chat_interface_wrapper] = gr.update(visible=True)
            updates[output_tabs] = gr.update(selected=selected_models[0])

        for model in selected_models:
            histories[model].append({'role': 'user', 'content': user_message})
            histories[model].append({'role': 'assistant', 'content': "..."})

        chatbot_updates = {chatbots[model]: histories[model] for model in selected_models}
        updates.update(chatbot_updates)
        yield updates

        try:
            if current_phase == "ANALYSIS_PENDING":
                api_endpoint = f"{API_URL}/analyze_mission_multi_stream"
                payload = {"mission_query_zh": user_message, "selected_models": selected_models}
                pipeline_steps = ANALYSIS_PIPELINE_STEPS
                for model in selected_models:
                    histories[model][-1]['content'] = "💭 **第一階段：任務分析中...**"
            else:
                api_endpoint = f"{API_URL}/query_components_multi_stream"
                payload = {"user_input_zh": user_message, "phase1_analysis_map_en": phase1_map, "summaries_map": summaries_map, "selected_models": selected_models}
                pipeline_steps = QUERY_PIPELINE_STEPS
                for model in selected_models:
                    histories[model][-1]['content'] = "💭 **第二階段：元件查詢中...**"

            initial_status_md = create_status_markdown(selected_models, pipeline_steps)
            chatbot_updates = {chatbots[model]: histories[model] for model in selected_models}
            yield {status_display: gr.update(value=initial_status_md, visible=True), **chatbot_updates}
            
            current_status_md = initial_status_md
            with requests.post(api_endpoint, json=payload, stream=True, timeout=600) as response:
                response.raise_for_status()
                for line in response.iter_lines():
                    if line and line.decode('utf-8').startswith('data: '):
                        data_str = line.decode('utf-8')[6:]
                        try:
                            data = json.loads(data_str)
                            if data.get("type") == "done": break
                            model_name = data.get("model_name")
                            if not model_name: continue
                            
                            content = data.get("content", {})
                            if data.get("type") == "status":
                                current_status_md = update_status_markdown(current_status_md, data, pipeline_steps)
                                yield {status_display: current_status_md}
                            elif data.get("type") == "full_response":
                                if current_phase == "ANALYSIS_PENDING":
                                    bot_response = format_single_analysis_response(content)
                                    phase1_map[model_name] = content.get("analysis_result_en", "")
                                else:
                                    bot_response = format_single_query_response(content)
                                histories[model_name][-1]['content'] = bot_response
                                yield {chatbots[model_name]: histories[model_name], phase1_analysis_map_state: phase1_map}
                            elif data.get("type") == "summary":
                                summaries_map[model_name] = content
                                yield {summaries_map_state: summaries_map}
                            elif data.get("type") == "error":
                                histories[model_name][-1]['content'] = f"❌ **執行時發生錯誤:**\n`{content}`"
                                yield {chatbots[model_name]: histories[model_name]}
                        except json.JSONDecodeError:
                            print(f"Failed to decode JSON from stream: {data_str}")
            if current_phase == "ANALYSIS_PENDING":
                current_phase = "QUERY_READY"
                for model in selected_models:
                    histories[model].append({'role': 'assistant', 'content': "✅ **任務分析完成！** 現在可以針對細節提問。"})
                chatbot_updates = {chatbots[model]: histories[model] for model in selected_models}
                yield {phase_state: current_phase, **chatbot_updates}
        
        except requests.exceptions.RequestException as e:
            err_msg = f"⚠️ **網路連線錯誤:**\n`{e}`"
            for model in selected_models: histories[model][-1]['content'] = err_msg
            yield {**{chatbots[m]: h for m, h in histories.items()}}
        except Exception as e:
            err_msg = f"⚠️ **處理請求時發生未預期的錯誤:**\n`{e}`"
            for model in selected_models: histories[model][-1]['content'] = err_msg
            yield {**{chatbots[m]: h for m, h in histories.items()}}
        
        finally:
            # Re-enable the input box at the very end
            yield {msg_input: gr.update(interactive=True)}
    
    # --- 事件綁定 ---
    all_states = [phase_state, chat_histories_state, phase1_analysis_map_state, summaries_map_state]
    all_ui_comps = [msg_input, status_display, welcome_screen, chat_interface_wrapper, output_tabs] + list(chatbots.values())
    all_outputs = all_ui_comps + all_states

    def clear_all_states():
        initial_histories = {model_name: [] for model_name in MODEL_CONFIG_ORDER}
        updates = {
            phase_state: "ANALYSIS_PENDING", 
            phase1_analysis_map_state: {}, 
            summaries_map_state: {},
            chat_histories_state: initial_histories, 
            msg_input: "", 
            status_display: gr.update(visible=False),
            welcome_screen: gr.update(visible=True), 
            chat_interface_wrapper: gr.update(visible=False),
        }
        for chatbot_component in chatbots.values():
            updates[chatbot_component] = []
        return updates
    
    submit_inputs = [msg_input, model_checkboxes, phase_state, chat_histories_state, phase1_analysis_map_state, summaries_map_state]
    msg_input.submit(fn=handle_submit, inputs=submit_inputs, outputs=all_outputs)
    send_btn.click(fn=handle_submit, inputs=submit_inputs, outputs=all_outputs)
    clear_btn.click(fn=clear_all_states, inputs=None, outputs=all_outputs, queue=False)

if __name__ == "__main__":
    demo.queue().launch(server_name="0.0.0.0", server_port=7860)
