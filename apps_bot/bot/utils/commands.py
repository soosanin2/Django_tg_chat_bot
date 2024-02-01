from aiogram import Bot
from aiogram.types import  BotCommand, BotCommandScopeDefault

async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='start bot'
            ),
        BotCommand(
            command='help',
            description='info from bot'
            ),
        BotCommand(
            command='get_sticker',
            description='дать последний присланный стикер'
            ),
        BotCommand(
            command='stget_inlineart',
            description='показать инлайн клавиатуру'
            ),

    ]