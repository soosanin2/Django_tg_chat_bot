import logging
from pprint import pprint

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from environs import Env

from Config.settings import BOT_TOKEN

dp = Dispatcher()
env = Env()
env.read_env()

logger = logging.getLogger(__name__)

bot = Bot(token=BOT_TOKEN, parse_mode='HTML')


@dp.message(CommandStart())
async def press_start(message: Message):
    await message.answer(text=f'Hi<b> {message.chat.username}!</b> ')
    logger.info(f'{message.chat.username}')


@dp.message(Command(commands='help'))
async def press_help(message: Message):
    await message.answer(text="No help =)")


@dp.message()
async def echo_message(message: Message):
    if message.text:
        await message.answer(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
