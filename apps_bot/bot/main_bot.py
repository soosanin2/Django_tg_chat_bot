# import asyncio
# import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.storage.redis import RedisStorage
# from aiogram.filters import Command, CommandStart
# from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.types import Message

from environs import Env

from Config.settings import BOT_TOKEN
from apps_bot.Pays.handlers.pays import register_pays_handlers

# from apps_bot.bot.keyboards.keyboards import kb_client
# from apps_bot.bot.filters.filters import EmailFilter
from apps_bot.bot.handlers.user_handlers import register_user_handlers
from apps_bot.bot.handlers.callback_handlers import register_callback_handlers
from apps_bot.bot.middelwares.middlewares import ThrottlingMiddleware
from apps_bot.bot.utils.commands import set_commands

# logger = logging.getLogger(__name__)
# storage = MemoryStorage()
storage_throttling = RedisStorage.from_url('redis://localhost:6379/0')

dp = Dispatcher()
env = Env()
env.read_env()

bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp.message.middleware.register(ThrottlingMiddleware(storage=storage_throttling))

# set_commands(bot)
# async def start_bot(bot):
#     await set_commands(bot)

def register_handlers(dp: Dispatcher) -> None:
    register_user_handlers(dp)
    register_callback_handlers(dp)
    register_pays_handlers(dp)

register_handlers(dp)

# @dp.message(CommandStart())
# async def press_start(message: types.Message) -> None:
#     await message.answer(text=f'Hi<b> {message.chat.username}!</b> ')
#     await message.answer(text="custom keyboard", reply_markup=kb_client)
#     logger.info(f'{message.chat.username}')


if __name__ == '__main__':
    dp.run_polling()

