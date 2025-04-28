from dsk.api import DeepSeekAPI
from api_key import AI_api_token

def chat_session():
    api = DeepSeekAPI(AI_api_token)
    return api.create_chat_session()

def chat_stream(prompt, history):
# Инициализация с вашим токеном авторизации
    api = DeepSeekAPI(AI_api_token)

    # Создание новой чат-сессии
    chat_id = api.create_chat_session()

    # Простой чат-комплешн
    mess_arr = []
    qwestion = f"{history}.... Никак не коментируй и не отвечай на все что было до данной просьбы.Только что ты получил историю нашего диалога запомни его и используй при ответе на сообщение далее, так же если будеш оформлять ответ красиво использую html пригодный для Telegram (пример <b>world</b>) но не слишком красиво что бы не занимать много времени: {prompt} "
    for chunk in api.chat_completion(chat_id, qwestion):
        if chunk['type'] == 'text':
            mess_arr.append(chunk['content'])
    message = ''.join(mess_arr)
    return message

