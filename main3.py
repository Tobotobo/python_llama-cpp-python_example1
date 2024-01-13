# 【ローカルLLM】Gradioとllama-cpp-pythonで日本語チャットボットを作る
# https://note.com/bakushu/n/n9b7b044655f6

# ウェブUIの起動
import os
import gradio as gr
import copy
import time
from llama_cpp import Llama

llm = Llama(
    # model_path="ggml-model-q4_m.gguf",
    model_path="C:/models/ELYZA-japanese-Llama-2-7b-instruct-q5_0.gguf",
    n_ctx=2048,
    # n_gpu_layers=100, #CPUで実行する場合は削除
)

history = []

system_message = """
あなたはAIアシスタントです。
"""

def generate_text(message, history):
    temp = ""
    input_prompt = f"{system_message}"
    for interaction in history:
        input_prompt = input_prompt + "\nUSER: " + str(interaction[0]) + "\nASSISTANT: " + str(interaction[1])
    input_prompt = input_prompt + "\nUSER: " + str(message) + "\nASSISTANT: "

    output = llm.create_completion(
        input_prompt,
        temperature=0.7,
        top_p=0.3,
        top_k=40,
        repeat_penalty=1.1,
        max_tokens=1024,
        stop=[
            "ASSISTANT:",
            "USER:",
            "SYSTEM:",
        ],
        stream=True,
    )
    for out in output:
        stream = copy.deepcopy(out)
        temp += stream["choices"][0]["text"]
        yield temp

    history = ["init", input_prompt]


demo = gr.ChatInterface(
    generate_text,
    title="Japanese chatbot using llama-cpp-python",
    description="",
    # examples=["日本の四国にある県名を挙げてください。"],
    # cache_examples=True,
    retry_btn=None,
    undo_btn="Remove last",
    clear_btn="Clear all",
)
# demo.queue(concurrency_count=1, max_size=5)
# demo.launch(debug=True, share=True)
demo.launch()
