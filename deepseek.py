import requests
from api_key import AI_api_token

TOKEN = AI_api_token

QWEN_URL = "https://chat.qwenlm.ai/api/chat/completions"
QWEN_HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/237.84.2.178 Safari/537.36"
}

messages = [
    {"role": "user", "content": "Привет!", "extra": {}, "chat_type": "t2t"},
]

payload = {
    "chat_type": "t2t",
    "messages": messages,
    "model": "qwen-max-latest",
    "stream": False
}

response = requests.post(QWEN_URL, headers=QWEN_HEADERS, json=payload)

if response.status_code == 200:
    result = response.json()
    print("Ответ от нейросети:", result["choices"][0]["message"]["content"])
else:
    print(f"Ошибка при отправке запроса: {response.status_code}")
    print("Текст ошибки:", response.text)