# apps_bot/bot/management/commands/runserver_with_bot.py
import asyncio
from django.core.management.base import BaseCommand
from django_extensions.management.commands.runserver_plus import Command as RunServerCommand
from apps_bot.bot.main_bot import bot, dp


class Command(RunServerCommand):
    help = 'Run both Django server and Telegram bot'

    def handle(self, *args, **options):
        # Start the bot in a separate asyncio loop
        asyncio.create_task(dp.start_polling(bot, skip_updates=True))

        # Now, call the parent handle method to start the Django server
        super().handle(*args, **options)
