from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from environs import Env

dp = Dispatcher()
env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN, parse_mode='HTML')


@dp.message(CommandStart())
async def press_start(message: Message):
    await message.answer(text='<b>Hi!</b> qwert')


@dp.message(Command(commands='help'))
async def press_help(message: Message):
    await message.answer(text="No help =)")





@dp.message()
async def echo_message(message: Message):
    await message.answer(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
    from django.core.management import execute_from_command_line
