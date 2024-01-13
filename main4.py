# Gradioとは？ Pythonで機械学習Webアプリケーションをサクッと作ろう！
# https://aiacademy.jp/media/?p=3469

import random
import gradio as gr

def get_foturne(your_name):
    fortune_lists = ['大吉', '吉', '小吉', '凶', '末吉']
    fortune_result = random.choice(fortune_lists)
    return your_name + "さんの今日の運勢は・・・" + fortune_result + "です"


demo = gr.Interface(fn=get_foturne,
                    inputs="text",
                    outputs="text")
demo.launch()