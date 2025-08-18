import gradio as gr

def chat_fn(message, history):
    # 三個不同輸出 (這裡先假裝，之後換成你的 LLM)
    responses = [
        f"輸出 1: {message}",
        f"輸出 2: {message.upper()}",
        f"輸出 3: {message[::-1]}"
    ]

    # 回傳三個獨立訊息
    return [(message, r) for r in responses]

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="輸入訊息")

    def respond(message, chat_history):
        responses = chat_fn(message, chat_history)
        for user, bot in responses:
            chat_history.append((user, bot))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()
