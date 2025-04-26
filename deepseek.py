from dsk.api import DeepSeekAPI

# Инициализация с вашим токеном авторизации
api = DeepSeekAPI("Z6QZ+1OTzZIp2XqZDs4qUN+tukCZwy2u5PhLzRuZJE+5DNHLRaF5FwOjTr3yF5Kk")

# Создание новой чат-сессии
chat_id = api.create_chat_session()

# Простой чат-комплешн
prompt = "Что такое Python?"
for chunk in api.chat_completion(chat_id, prompt):
    if chunk['type'] == 'text':
        print(chunk['content'], end='', flush=True)