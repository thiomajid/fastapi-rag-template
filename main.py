import gradio as gr

# from app.embeddings import create_embeddings
# from app.query_engine import model_pipeline

with gr.Blocks() as demo:
    gr.Markdown("# Clarins chatbot demo")
    with gr.Row():
        with gr.Column() as col:
            question = gr.Textbox(label="Votre question", lines=7)
            run_query_btn = gr.Button(variant="primary", value="Chercher")
            embedding_btn = gr.Button(value="Create embeddings")
        with gr.Column():
            output = gr.Textbox(label="Output", lines=10)

    # event = run_query_btn.click(
    #     model_pipeline,
    #     inputs=[question],
    #     outputs=[output],
    # )
    # embedding_btn.click(create_embeddings)


demo.launch(
    server_name="0.0.0.0",
    server_port=8000,
    share=True,
)
