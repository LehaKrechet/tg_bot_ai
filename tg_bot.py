from api_key import tg_api_token
import asyncio
import logging
import sys
import deepseek 
import file_worker
from api_key import AI_api_token

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


TOKEN = tg_api_token



dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
    file_worker.file_writer_personal(message.from_user.full_name, "/start", f"Hello, {html.bold(message.from_user.full_name)}!")

@dp.message(Command("service"))
async def service_info(message: Message):

    await message.answer(f"""Chat full_name: {message.chat.full_name}\n 
Chat id: {message.chat.id}\n
User full_name: {message.from_user.full_name}\n
User id: {message.from_user.id}""")

@dp.message()
async def echo_handler(message: Message) -> None:
    try:

        user_name = message.from_user.full_name
        group_name = message.chat.full_name

        if user_name != group_name:
            history_name = group_name
            file_worker.file_writer_group(group_name, user_name, message.text, '')
        else:
            history_name = f"{user_name}_individual"

        answer = deepseek.chat_stream(message.text, file_worker.file_reader(history_name))
        await message.answer(answer, parse_mode=ParseMode.HTML)

        if user_name != group_name:
            file_worker.file_writer_group(group_name, user_name, message.text, answer)
        else:
            file_worker.file_writer_personal(user_name, message.text, answer)
        

    except TypeError:
        await message.answer("Error")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())