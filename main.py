import asyncio
from telebot.types import Update
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from typing import Callable, Dict, Any, Awaitable
from aiogram.client.default import DefaultBotProperties

from config.db import sync_engine
from config.globals import config
from service.todo import TodoService

default = DefaultBotProperties(parse_mode="Markdown")
bot = Bot(token=config.TELEGRAM_TOKEN, default=default)
dp = Dispatcher()

todoService = TodoService()

@dp.message.middleware()
async def database_transaction_middleware(
    handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
    event: Update,
    data: Dict[str, Any]
) -> Any:

    if data["event_from_user"].id != config.MY_TELEGRAM_ID:
        await bot.send_message(chat_id=data["event_chat"].id, text="⛔ You are not allowed to use this bot")
        return
    await handler(event, data)

@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.answer("Привет! Добро пожаловать в AI TODODO! Выбери действие из списка команд")

@dp.message(Command('id'))
async def send_welcome(message: types.Message):
    await message.answer(f"`{message.from_user.id}`")

@dp.message(Command('today_todos'))
async def send_today_todos(message: types.Message):
    result = todoService.get_today()
    await message.answer(text=result)

@dp.message()
async def post_todo(message: types.Message):
    result = todoService.add(message.text)

    await message.answer(result)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Shutting down")
