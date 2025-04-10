from typing import Callable, Awaitable

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart, Command
from telebot.types import Update
from typing import Dict, Any, Awaitable

from config.globals import config
import asyncio

allowed_users = [686364607]

default = DefaultBotProperties(parse_mode="Markdown")
bot = Bot(token=config.TELEGRAM_TOKEN, default=default)
dp = Dispatcher()

@dp.message.middleware()
async def database_transaction_middleware(
    handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
    event: Update,
    data: Dict[str, Any]
) -> Any:
    if data["event_from_user"].id not in allowed_users:
        await bot.send_message(chat_id=data["event_chat"].id, text="⛔ You are not allowed to use this bot")
        return
    await handler(event, data)

@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.answer("Привет! Добро пожаловать в AI TODODO! Выбери действие из списка команд")

@dp.message(Command('id'))
async def send_welcome(message: types.Message):
    await message.answer(f"`{message.from_user.id}`")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Shutting down")