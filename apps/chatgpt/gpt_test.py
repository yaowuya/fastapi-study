import os

from openai import OpenAI

CHAT_GPT_KEY = "你的gpt key"
os.environ["HTTP_PROXY"] = "http://127.0.0.1:10809"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:10809"
client = OpenAI(
    api_key=CHAT_GPT_KEY,
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "你好，请问你是谁"
        }
    ]
)

print(completion.choices[0].message)
