import gradio as gr

def chat_fn(message, history):
    # 這裡之後換成你的 LLM 輸出
    responses = [
        f"輸出 1: {message}",
        f"輸出 2: {message.upper()}",
        f"輸出 3: {message[::-1]}"
    ]

    # 回傳三個獨立訊息
    return [(message, r) for r in responses]

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="輸入訊息", placeholder="輸入後按 Enter", lines=1)

    def respond(message, chat_history):
        responses = chat_fn(message, chat_history)
        for user, bot in responses:
            chat_history.append((user, bot))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])  # 綁定 Enter 送出

demo.launch()
