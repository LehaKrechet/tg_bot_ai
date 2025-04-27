from dsk.api import DeepSeekAPI
from api_key import AI_api_token

# Инициализация с вашим токеном авторизации
api = DeepSeekAPI(AI_api_token)

# Создание новой чат-сессии
chat_id = api.create_chat_session()

# Простой чат-комплешн
prompt = "Привет"
for chunk in api.chat_completion(chat_id, prompt):
    if chunk['type'] == 'text':
        print(chunk['content'], end='', flush=True)