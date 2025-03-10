import gradio as gr

with gr.Blocks() as demo:
    input_text = gr.Textbox(label="input")
    mode = gr.Radio(["textbox", "button"], value="textbox")

    @gr.render(inputs=[input_text, mode], triggers=[input_text.submit])
    def show_split(text, mode):
        if len(text) == 0:
            gr.Markdown("## No Input Provided")
        else:
            for letter in text:
                if mode == "textbox":
                    gr.Textbox(letter)
                else:
                    gr.Button(letter)

demo.launch(server_port=7870, share=True)
