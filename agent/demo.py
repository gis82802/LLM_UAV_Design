import gradio as gr

# 先用假的 function 佔位，之後換成你的 LLM
def chat_fn(message, history):
    # 這邊先回傳三個不同的輸出文字
    responses = [
        f"輸出 1: {message}",
        f"輸出 2: {message.upper()}",
        f"輸出 3: {message[::-1]}"
    ]

    # 把三個輸出組成一個 block
    combined_response = "\n---\n".join(responses)
    return combined_response

# 建立 ChatInterface
demo = gr.ChatInterface(
    fn=chat_fn,
    title="LLM 多輸出對話 Demo",
    description="輸入一句話，會得到三個輸出結果 (目前是 placeholder)"
)

demo.launch()
