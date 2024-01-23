#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import asyncio
import os
import sys
import subprocess
from multiprocessing import Process

from apps_bot.bot.main_bot import dp, bot


"""Раскоментировать для запуска бота и сервера одновременно

def run_bot():
    subprocess.run(["python", 'manage.py', 'run_bot'])

def run_server():
    '''Run administrative tasks.'''
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    bot_process = Process(target=run_bot)
    bot_process.start()

    run_server()

    bot_process.join()
"""



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
