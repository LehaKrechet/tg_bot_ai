from api_key import tg_api_token
import asyncio
import logging
import sys
from os import getenv
import deepseek 
import file_worker
from api_key import AI_api_token

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message


TOKEN = tg_api_token



dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
    file_worker.file_writer(message.from_user.full_name, "/start", f"Hello, {html.bold(message.from_user.full_name)}!")



@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        your_name = message.from_user.full_name
        answer = deepseek.chat_stream(message.text, file_worker.file_reader(your_name))
        await message.answer(answer, parse_mode=ParseMode.HTML)
        file_worker.file_writer(your_name, message.text, answer)

    except TypeError:
        await message.answer("Error")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())