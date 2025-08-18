import gradio as gr

def chat_fn(message, history):
    # 之後這邊換成你的 LLM (可以各自不同 prompt)
    return (
        f"Bot1 收到: {message}",
        f"Bot2 收到: {message.upper()}",
        f"Bot3 收到: {message[::-1]}"
    )

with gr.Blocks() as demo:
    with gr.Row():
        chatbot1 = gr.Chatbot(label="對話框 1")
        chatbot2 = gr.Chatbot(label="對話框 2")
        chatbot3 = gr.Chatbot(label="對話框 3")

    msg = gr.Textbox(label="輸入訊息", placeholder="輸入文字，按送出", lines=1)
    send = gr.Button("送出")

    def respond(message, history1, history2, history3):
        r1, r2, r3 = chat_fn(message, None)
        history1.append((message, r1))
        history2.append((message, r2))
        history3.append((message, r3))
        return "", history1, history2, history3

    send.click(respond, [msg, chatbot1, chatbot2, chatbot3],
                        [msg, chatbot1, chatbot2, chatbot3])

demo.launch()
