import gradio as gr

def chat_fn(message):
    return (
        {"role": "assistant", "content": f"Bot1 收到: {message}"},
        {"role": "assistant", "content": f"Bot2 收到: {message.upper()}"},
        {"role": "assistant", "content": f"Bot3 收到: {message[::-1]}"}
    )

with gr.Blocks() as demo:
    with gr.Row():
        chatbot1 = gr.Chatbot(label="對話框 1", type="messages")
        chatbot2 = gr.Chatbot(label="對話框 2", type="messages")
        chatbot3 = gr.Chatbot(label="對話框 3", type="messages")

    msg = gr.Textbox(label="輸入訊息", placeholder="輸入文字，按送出", lines=1)
    send = gr.Button("送出")

    def respond(message, history1, history2, history3):
        r1, r2, r3 = chat_fn(message)
        history1.append({"role": "user", "content": message})
        history1.append(r1)

        history2.append({"role": "user", "content": message})
        history2.append(r2)

        history3.append({"role": "user", "content": message})
        history3.append(r3)

        return "", history1, history2, history3

    send.click(respond, [msg, chatbot1, chatbot2, chatbot3],
                        [msg, chatbot1, chatbot2, chatbot3])

demo.launch()
