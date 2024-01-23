import logging

from django.core.management.base import BaseCommand

from apps_bot.bot.main_bot import bot, dp
import asyncio

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Запуск телеграм-бота'

    def handle(self, *args, **options):
        logging.basicConfig(
            level=logging.INFO,
            format='%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
        )

        logger.info('starting bot')
        asyncio.run(dp.start_polling(bot))




