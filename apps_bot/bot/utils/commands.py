from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

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
            command='new_inline_keyboard',
            description='показать инлайн клавиатуру'
            ),
        BotCommand(
            command='pay',
            description='Купить товар без доставки'
            ),
    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())
