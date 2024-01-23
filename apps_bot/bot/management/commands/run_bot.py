from django.core.management.base import BaseCommand
# from aiogram import Bot, Dispatcher

from apps_bot.bot.main_bot import BOT_TOKEN, bot, dp
import asyncio
from aiogram.filters import CommandStart
from aiogram.types import Message

class Command(BaseCommand):
    help = 'Запуск телеграм-бота'

    def handle(self, *args, **options):
        asyncio.run(dp.start_polling(bot))
