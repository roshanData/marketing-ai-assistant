import gradio as gr
import pandas as pd
from langchain_together import Together

def analyze(question):
    llm = Together(
        model="mistralai/Mistral-7B-Instruct-v0.1",
        together_api_key="PASTE_YOUR_KEY_HERE"  # 🔒 Remove before sharing!
    )
    return llm.invoke(f"Analyze marketing data: {question}")

with gr.Blocks() as demo:
    gr.Markdown("# 📊 Marketing AI Assistant")
    question = gr.Textbox(label="Ask about your data")
    output = gr.Textbox(label="Insights")
    question.submit(analyze, inputs=question, outputs=output)

demo.launch()