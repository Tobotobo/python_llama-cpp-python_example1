from llama_cpp import Llama
llm = Llama(model_path="C:/models/ELYZA-japanese-Llama-2-7b-instruct-q5_0.gguf")

while True:
    prompt = input("あなた: ")
    output = llm(
        f"[INST]<<SYS>>あなたは、役立つアシスタントです。<</SYS>>{prompt}[/INST]",
        max_tokens=500,
        stop=["System:", "User:", "Assistant:"],
        echo=False,
    )
    print("AI:", output['choices'][0]['text'].strip())
