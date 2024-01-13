# python_llama-cpp-python_example1

## 概要
llama-cpp-python をとりあえず適当に動かしてみた。

Python Bindings for llama.cpp  
https://github.com/abetlen/llama-cpp-python  

ELYZA-japanese-Llama-2-7b-instruct-gguf  
https://huggingface.co/mmnga/ELYZA-japanese-Llama-2-7b-instruct-gguf/blob/main/ELYZA-japanese-Llama-2-7b-instruct-q5_0.gguf

## 詳細

```
python -m venv .venv
./.venv/Scripts/Activate.ps1
```

```
pip install llama-cpp-python
pip install gradio
```

```
python main.py
python main2.py
python main3.py
python main4.py
```

## 環境

```
> python --version
Python 3.12.1

> systeminfo
OS 名:                  Microsoft Windows 10 Pro
OS バージョン:          10.0.19045 N/A ビルド 19045
システム製造元:         LENOVO
システム モデル:        20HQS1BJ00
システムの種類:         x64-based PC
プロセッサ:             1 プロセッサインストール済みです。
                        [01]: Intel64 Family 6 Model 142 Stepping 9 GenuineIntel ~2611 Mhz
BIOS バージョン:        LENOVO N1MET60W (1.45 ), 2020/02/17
物理メモリの合計:       16,027 MB
仮想メモリ: 最大サイズ: 18,459 MB
```

