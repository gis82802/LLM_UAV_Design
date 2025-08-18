import gradio as gr

def placeholder(user_input):
    return "", "", ""

demo = gr.Interface(
    fn=placeholder,
    inputs=gr.Textbox(label="輸入文字"),
    outputs=[
        gr.Textbox(label="輸出 1"),
        gr.Textbox(label="輸出 2"),
        gr.Textbox(label="輸出 3")
    ],
    title="LLM 輸入輸出 Demo",
    description="一個輸入，三個輸出 (LLM placeholder)"
)

demo.launch()
