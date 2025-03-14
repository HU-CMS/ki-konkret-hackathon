import gradio as gr

def greet(name, intensity):

	return "Hello, " + name + "!" * int(intensity) 


demo = gr.Interface( fn=greet, inputs=["text", "slider"], 
			       outputs=["text"]
                    ) 

demo.launch(server_port=7860, share=True)
