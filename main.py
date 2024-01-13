from llama_cpp import Llama
# プロンプトを記入
prompt = """[INST]<<SYS>>あなたは、役立つアシスタントです。<</SYS>>1+1の答えは何ですか？[/INST]"""
# ダウンロードしたModelをセット.
llm = Llama(model_path="C:/models/ELYZA-japanese-Llama-2-7b-instruct-q5_0.gguf")
# 生成実行
output = llm(
    prompt,max_tokens=500,stop=["System:", "User:", "Assistant:"],echo=False,
)
print(output['choices'][0]['text'].strip())