import requests
import json
import base64
from api_key import AI_api_token


API_KEY = AI_api_token # внутри скобок свой апи ключ отсюда https://openrouter.ai/settings/keys
MODEL = "deepseek/deepseek-r1"

def encode_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()
            return base64.b64encode(file_content).decode('utf-8')
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None
    
def process_content(content):
    return content.replace('<think>', '').replace('</think>', '')

def chat_stream(prompt, file_path):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    messages = [{"role": "user", "content": prompt}]

    # Если указан файл, добавляем его
    if file_path:
        file_content = encode_file(file_path)
        if file_content:
            messages[0]["files"] = [{
                "type": "text/plain",  # измените на соответствующий MIME-тип
                "content": file_content
            }]
    # message.append([{"role": "user", "content": prompt}])
    data = {
        "model": MODEL,
        "messages": messages,
        "stream": True
    }

    with requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data,
        stream=True
    ) as response:
        if response.status_code != 200:
            print("Ошибка API:", response.status_code)
            return ""

        full_response = []
        
        for chunk in response.iter_lines():
            if chunk:
                chunk_str = chunk.decode('utf-8').replace('data: ', '')
                try:
                    chunk_json = json.loads(chunk_str)
                    if "choices" in chunk_json:
                        content = chunk_json["choices"][0]["delta"].get("content", "")
                        if content:
                            cleaned = process_content(content)
                            print(cleaned, end='', flush=True)
                            full_response.append(cleaned)
                except:
                    pass

        print()  # Перенос строки после завершения потока
        return ''.join(full_response)
def main():
    print("Чат с DeepSeek-R1 (by Antric)\nДля выхода введите 'exit'\n")

    while True:
        user_input = input("Вы: ")
        
        if user_input.lower() == 'exit':
            print("Завершение работы...")
            break
            
        print("DeepSeek-R1:", end=' ', flush=True)
        chat_stream(user_input)

if __name__ == "__main__":
    main()