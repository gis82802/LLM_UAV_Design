import gradio as gr

def chat_fn(message, history):
    # 之後這邊換成你的 LLM
    responses = [
        f"輸出 1: {message}",
        f"輸出 2: {message.upper()}",
        f"輸出 3: {message[::-1]}"
    ]
    return [(message, r) for r in responses]

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    with gr.Row():
        msg = gr.Textbox(label="輸入訊息", placeholder="請輸入文字", lines=1)
        send = gr.Button("送出")

    def respond(message, chat_history):
        responses = chat_fn(message, chat_history)
        for user, bot in responses:
            chat_history.append((user, bot))
        return "", chat_history

    send.click(respond, [msg, chatbot], [msg, chatbot])  # 綁定送出按鈕

demo.launch()
