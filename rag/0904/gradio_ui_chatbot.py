# gradio_ui_chatbot.py

import gradio as gr
import requests
import json
import re
from copy import deepcopy
from config import MODEL_CONFIGURATIONS

# --- 基礎設定 ---
API_URL = "http://127.0.0.1:7777"
MODEL_CONFIG_ORDER = list(MODEL_CONFIGURATIONS.keys())

# --- 流程步驟定義 ---
ANALYSIS_PIPELINE_STEPS = ["翻譯任務需求", "執行初步分析", "翻譯分析結果"]
QUERY_PIPELINE_STEPS = ["翻譯使用者問題", "分析查詢意圖(RAG)", "路由查詢(選擇模板)", "檢索相關文件", "生成 RAG 回答", "翻譯最終結果", "更新對話摘要"]

# --- 自訂 CSS ---
CUSTOM_CSS = """
body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
#title_md { text-align: center; color: #333; }
.gradio-container { max-width: 1280px !important; margin: auto !important; }
#main-col { gap: 20px; }
#status-display-wrapper { padding: 12px; border: 1px solid #e0e0e0; border-radius: 8px; background-color: #f9f9f9; }
.gr-tab-item { flex-grow: 1; text-align: center; }
#welcome-screen { text-align: center; padding: 40px; }
.gr-prose { white-space: pre-wrap; } /* 讓說明文字可以換行 */
"""

# --- 格式化與輔助函式 ---
def format_single_analysis_response(result: dict) -> str:
    if not result: return "❌ 模型分析失敗，請檢查後端日誌。"
    model_name = result.get('model_name', '未知模型')
    analysis = result.get('analysis_result_zh', '無結果')
    return f"### 🧠 **模型: {model_name}**\n{analysis}\n\n"

# (*** 修改 ***) 函式增加 model_name 參數，並在輸出中加入標頭
def format_single_query_response(data: dict, model_name: str) -> str:
    formatted_text = f"### 🧠 **模型: {model_name}**\n"
    if data.get("error"):
        formatted_text += f"❌ **執行時發生錯誤:**\n`{data['error']}`\n\n"
        return formatted_text
        
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
    md = "⏳ **執行中...** 請等待目前請求完成後再修改模型組合。\n\n"
    md += "### 🚀 執行狀態\n"
    for model_name in selected_models:
        safe_model_name = re.sub(r'[^a-zA-Z0-9]', '-', model_name)
        md += f"<div id='status-{safe_model_name}'><p><strong>{model_name}</strong></p>"
        for i, step in enumerate(steps):
            md += f"<p id='step-{safe_model_name}-{i}' style='margin: 2px 0 2px 20px;'>⚪ {step}</p>"
        md += "</div>\n"
    return md

def update_status_markdown(current_md: str, event: dict, steps: list) -> str:
    model_name, step_index, status, error_msg = event.get("model_name"), event.get("step_index"), event.get("status"), event.get("error")
    if model_name is None or step_index is None or status is None or step_index >= len(steps): return current_md
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
    pending_model_state = gr.State(None)
    last_run_models_state = gr.State([])

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
                            chatbots[model_name] = gr.Chatbot(label=f"對話紀錄 ({model_name})", height=680, type='messages', elem_id=f"chatbot_{re.sub(r'[^a-zA-Z0-9]', '_', model_name)}", show_copy_button=True)
            with gr.Row(elem_id="input-row"):
                msg_input = gr.Textbox(placeholder="請在此輸入任務需求或查詢問題...", scale=9, container=False, elem_id="msg-input")
                send_btn = gr.Button("送出", variant="primary", min_width=100)
        with gr.Column(scale=1):
            with gr.Group():
                gr.Markdown("### ⚙️ 模型執行選項")
                model_checkboxes = gr.CheckboxGroup(choices=MODEL_CONFIG_ORDER, label="選擇要執行的模型組合", value=[MODEL_CONFIG_ORDER[0]] if MODEL_CONFIG_ORDER else [])
            
            with gr.Group(visible=False) as history_clone_group:
                clone_info_md = gr.Markdown()
                with gr.Group(visible=False) as new_add_choice_group:
                    new_add_radio = gr.Radio(choices=["從空白對話開始", "同步最新的對話紀錄"], label="請選擇處理方式")
                    new_add_details_md = gr.Markdown(visible=False)
                with gr.Group(visible=False) as re_add_choice_group:
                    re_add_radio = gr.Radio(choices=["繼續上次的對話", "同步最新的對話紀錄"], label="請選擇處理方式")
                    re_add_details_md = gr.Markdown(visible=False)
                with gr.Group(visible=False) as simple_clone_group:
                    simple_clone_radio = gr.Radio(label="請選擇要複製的對話歷史來源")
                
                with gr.Row():
                    clone_confirm_btn = gr.Button("確認", variant="primary")
                    clone_cancel_btn = gr.Button("取消")

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
        
        updates = {
            msg_input: gr.update(value="", interactive=False),
            send_btn: gr.update(interactive=False),
            model_checkboxes: gr.update(interactive=False),
            history_clone_group: gr.update(visible=False)
        }
        if current_phase == "ANALYSIS_PENDING":
            updates[welcome_screen] = gr.update(visible=False)
            updates[chat_interface_wrapper] = gr.update(visible=True)
            updates[output_tabs] = gr.update(selected=selected_models[0])

        for model in selected_models:
            if not histories.get(model): histories[model] = []
            histories[model].append({'role': 'user', 'content': user_message})
            histories[model].append({'role': 'assistant', 'content': "..."})

        chatbot_updates = {chatbots[model]: histories[model] for model in selected_models}
        updates.update(chatbot_updates)
        yield updates

        try:
            if current_phase == "ANALYSIS_PENDING":
                wait_message = "💭 **第一階段：任務分析中，請稍候...**"
                api_endpoint = f"{API_URL}/analyze_mission_multi_stream"
                payload = {"mission_query_zh": user_message, "selected_models": selected_models}
                pipeline_steps = ANALYSIS_PIPELINE_STEPS
            else:
                wait_message = "💭 **第二階段：元件查詢中，請稍候...**"
                api_endpoint = f"{API_URL}/query_components_multi_stream"
                payload = {"user_input_zh": user_message, "phase1_analysis_map_en": phase1_map, "summaries_map": summaries_map, "selected_models": selected_models}
                pipeline_steps = QUERY_PIPELINE_STEPS
            
            for model in selected_models:
                histories[model][-1]['content'] = wait_message
            yield {**{chatbots[model]: histories[model] for model in selected_models}}

            current_status_md = create_status_markdown(selected_models, pipeline_steps)
            yield {status_display: gr.update(value=current_status_md, visible=True)}
            
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
                                else:
                                    # (*** 修改 ***) 呼叫時傳入 model_name
                                    bot_response = format_single_query_response(content, model_name)
                                histories[model_name][-1]['content'] = bot_response
                                yield {chatbots[model_name]: histories[model_name], phase1_analysis_map_state: phase1_map}
                            elif data.get("type") == "summary":
                                summaries_map[model_name] = content
                                yield {summaries_map_state: summaries_map}
                            elif data.get("type") == "error":
                                histories[model_name][-1]['content'] = f"❌ **執行時發生錯誤:**\n`{content}`"
                                yield {chatbots[model_name]: histories[model_name]}
                        except json.JSONDecodeError: print(f"Failed to decode JSON from stream: {data_str}")
            
            final_updates = {}
            if current_phase == "ANALYSIS_PENDING":
                is_successful = any("錯誤" not in h[-1]['content'] and "..." not in h[-1]['content'] for m, h in histories.items() if m in selected_models and h)
                if is_successful:
                    current_phase = "QUERY_READY"
                    for model in selected_models:
                         if "錯誤" not in histories[model][-1]['content'] and "..." not in histories[model][-1]['content']:
                             histories[model].append({'role': 'assistant', 'content': "✅ **任務分析完成！** 現在可以針對細節提問。"})
                    final_updates[phase_state] = current_phase
                    final_updates.update({chatbots[model]: histories[model] for model in selected_models})

            final_updates[last_run_models_state] = selected_models
            yield final_updates

        except requests.exceptions.RequestException as e:
            err_msg = f"⚠️ **網路連線錯誤:**\n`{e}`"
            for model in selected_models: histories[model][-1]['content'] = err_msg
            yield {**{chatbots[m]: h for m, h in histories.items() if m in selected_models}}
        except Exception as e:
            err_msg = f"⚠️ **處理請求時發生未預期的錯誤:**\n`{e}`"
            for model in selected_models: histories[model][-1]['content'] = err_msg
            yield {**{chatbots[m]: h for m, h in histories.items() if m in selected_models}}
        finally:
            yield {
                msg_input: gr.update(interactive=True),
                send_btn: gr.update(interactive=True),
                model_checkboxes: gr.update(interactive=True),
                status_display: gr.update(visible=False, value="")
            }
    
    def handle_model_selection_change(current_selection, last_run_models, histories):
        active_models = last_run_models if last_run_models else []
        newly_added = list(set(current_selection) - set(active_models))
        
        if not newly_added or not active_models:
            return {
                history_clone_group: gr.update(visible=False), 
                pending_model_state: None,
                new_add_choice_group: gr.update(visible=False),
                re_add_choice_group: gr.update(visible=False),
                simple_clone_group: gr.update(visible=False)
            }

        new_model_to_process = newly_added[0]
        
        if histories.get(new_model_to_process):
            info_text = f"檢測到您正在重新啟用模型 **{new_model_to_process}**，它保留了上次的對話紀錄。請問您希望如何處理？"
            return {
                history_clone_group: gr.update(visible=True), clone_info_md: info_text,
                new_add_choice_group: gr.update(visible=False), re_add_choice_group: gr.update(visible=True), 
                simple_clone_group: gr.update(visible=False), pending_model_state: new_model_to_process
            }
        else:
            info_text = f"檢測到新增模型 **{new_model_to_process}**。請問您希望如何開始？"
            return {
                history_clone_group: gr.update(visible=True), clone_info_md: info_text,
                new_add_choice_group: gr.update(visible=True), re_add_choice_group: gr.update(visible=False),
                simple_clone_group: gr.update(visible=False), pending_model_state: new_model_to_process
            }

    def update_re_add_details(choice):
        if choice == "繼續上次的對話": return gr.update(visible=True, value="**說明**：模型將使用它自己舊的歷史紀錄。它會錯過您在它被停用期間的對話內容，可能導致**上下文斷層**，但能保持自身對話的連貫性。")
        elif choice == "同步最新的對話紀錄": return gr.update(visible=True, value="**說明**：模型將**放棄**自己舊的紀錄，並從您選擇的另一個活躍模型那裡**複製一份完整的新歷史紀錄**，以確保跟上最新的進度，避免上下文錯亂。")
        return gr.update(visible=False)
    
    def update_new_add_details(choice):
        if choice == "從空白對話開始": return gr.update(visible=True, value="**說明**：此模型將作為一個全新的協作者加入，不包含任何先前的對話歷史。")
        elif choice == "同步最新的對話紀錄": return gr.update(visible=True, value="**說明**：模型將從您選擇的另一個活躍模型那裡**複製一份完整的新歷史紀錄**，以確保能立即跟上團隊的最新進度。")
        return gr.update(visible=False)

    def execute_confirm_action(pending_model, re_add_choice, new_add_choice, simple_clone_source, last_run_models, histories, phase1_map, summaries_map):
        if not pending_model: return {}
        
        updates = {}
        active_models = last_run_models if last_run_models else []

        if simple_clone_source:
            source_model = simple_clone_source
            histories[pending_model] = deepcopy(histories.get(source_model, []))
            phase1_map[pending_model] = deepcopy(phase1_map.get(source_model, ""))
            summaries_map[pending_model] = deepcopy(summaries_map.get(source_model, ""))
            updates[chatbots[pending_model]] = histories[pending_model]
            gr.Info(f"已將 '{source_model}' 的歷史紀錄成功複製到 '{pending_model}'。")
            
            if pending_model not in last_run_models: last_run_models.append(pending_model)

            updates.update({
                last_run_models_state: last_run_models, chat_histories_state: histories, 
                phase1_analysis_map_state: phase1_map, summaries_map_state: summaries_map,
                history_clone_group: gr.update(visible=False), pending_model_state: None, 
                re_add_radio: None, new_add_radio: None, simple_clone_radio: None
            })
            return updates

        if re_add_choice:
            if re_add_choice == "繼續上次的對話":
                gr.Info(f"模型 '{pending_model}' 將繼續使用其先前的對話紀錄。")
                if pending_model not in last_run_models: last_run_models.append(pending_model)
                updates.update({
                    last_run_models_state: last_run_models, history_clone_group: gr.update(visible=False), 
                    pending_model_state: None, re_add_radio: None
                })
                return updates
            elif re_add_choice == "同步最新的對話紀錄":
                info_text = f"請為模型 **{pending_model}** 選擇一個要同步的對話歷史來源。"
                return {
                    clone_info_md: info_text, re_add_choice_group: gr.update(visible=False),
                    new_add_choice_group: gr.update(visible=False),
                    simple_clone_group: gr.update(visible=True),
                    simple_clone_radio: gr.update(choices=active_models, value=active_models[0]),
                }

        if new_add_choice:
            if new_add_choice == "從空白對話開始":
                gr.Info(f"模型 '{pending_model}' 將從一個空白的對話開始。")
                histories[pending_model] = []
                if pending_model not in last_run_models: last_run_models.append(pending_model)
                updates.update({
                    chat_histories_state: histories, last_run_models_state: last_run_models,
                    history_clone_group: gr.update(visible=False), pending_model_state: None, new_add_radio: None
                })
                return updates
            elif new_add_choice == "同步最新的對話紀錄":
                info_text = f"請為新模型 **{pending_model}** 選擇一個要同步的對話歷史來源。"
                return {
                    clone_info_md: info_text, new_add_choice_group: gr.update(visible=False),
                    re_add_choice_group: gr.update(visible=False),
                    simple_clone_group: gr.update(visible=True),
                    simple_clone_radio: gr.update(choices=active_models, value=active_models[0]),
                }
        
        return {history_clone_group: gr.update(visible=False)}

    def cancel_clone(last_run_models):
        return {
            history_clone_group: gr.update(visible=False),
            model_checkboxes: gr.update(value=last_run_models if last_run_models else [])
        }
    
    all_states = [phase_state, chat_histories_state, phase1_analysis_map_state, summaries_map_state, pending_model_state, last_run_models_state]
    all_ui_comps = [msg_input, send_btn, status_display, welcome_screen, chat_interface_wrapper, output_tabs, model_checkboxes] + list(chatbots.values())
    clone_ui_comps = [history_clone_group, clone_info_md, new_add_choice_group, new_add_radio, new_add_details_md, re_add_choice_group, re_add_radio, re_add_details_md, simple_clone_group, simple_clone_radio]
    all_outputs = all_ui_comps + clone_ui_comps + all_states

    def clear_all_states():
        initial_histories = {model_name: [] for model_name in MODEL_CONFIG_ORDER}
        return {
            phase_state: "ANALYSIS_PENDING", 
            phase1_analysis_map_state: {}, 
            summaries_map_state: {},
            chat_histories_state: initial_histories, 
            pending_model_state: None,
            last_run_models_state: [],
            msg_input: "", 
            status_display: gr.update(visible=False, value=""), 
            welcome_screen: gr.update(visible=True), 
            chat_interface_wrapper: gr.update(visible=False), 
            history_clone_group: gr.update(visible=False),
            **{chatbot: [] for chatbot in chatbots.values()}
        }

    submit_inputs = [msg_input, model_checkboxes, phase_state, chat_histories_state, phase1_analysis_map_state, summaries_map_state]
    msg_input.submit(fn=handle_submit, inputs=submit_inputs, outputs=all_outputs)
    send_btn.click(fn=handle_submit, inputs=submit_inputs, outputs=all_outputs)
    clear_btn.click(fn=clear_all_states, inputs=None, outputs=all_outputs, queue=False)

    model_checkboxes.change(fn=handle_model_selection_change, inputs=[model_checkboxes, last_run_models_state, chat_histories_state], outputs=[history_clone_group, clone_info_md, new_add_choice_group, re_add_choice_group, simple_clone_group, simple_clone_radio, pending_model_state])
    new_add_radio.change(fn=update_new_add_details, inputs=new_add_radio, outputs=new_add_details_md)
    re_add_radio.change(fn=update_re_add_details, inputs=re_add_radio, outputs=re_add_details_md)
    clone_confirm_btn.click(fn=execute_confirm_action, inputs=[pending_model_state, re_add_radio, new_add_radio, simple_clone_radio, last_run_models_state, chat_histories_state, phase1_analysis_map_state, summaries_map_state], outputs=all_outputs)
    clone_cancel_btn.click(fn=cancel_clone, inputs=[last_run_models_state], outputs=[history_clone_group, model_checkboxes])

if __name__ == "__main__":
    demo.queue(default_concurrency_limit=20).launch(server_name="0.0.0.0", server_port=7860)
