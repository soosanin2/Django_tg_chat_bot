import logging

from aiogram import types, F, Dispatcher
# from apps_bot.bot.main_bot import logger
from aiogram.filters import Command, CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message

from apps_bot.bot.keyboards.keyboards import kb_client
from apps_bot.bot.keyboards.inline_keyboards import inl_kb
from apps_bot.bot.filters.filters import EmailFilter, TwoWords, InText15
from apps_bot.bot.LEXICONES.LEXICON import LEXICONE_ALL, LEXICON_MAIN_MENU
from apps_bot.bot.utils.commands import set_commands

logger = logging.getLogger(__name__)
stic_dict = {'sticker_id': 'CAACAgIAAxkBAAIHgWWzgOskRP3A07G9XHHj9j-V9OW-AAJVPgAC-CqZSdQYG4ijLGxQNAQ'}


# @dp.message(CommandStart())
async def start_process(message: types.Message, bot) -> None:
    await message.answer(text=f'{LEXICONE_ALL["start"]}<strong>{message.chat.username} </strong>')
    await message.answer(text="custom keyboard", reply_markup=kb_client)
    await set_commands(bot)
    logger.info(f'{message.chat.username}')


# @dp.message(EmailFilter())
async def check_emile(message: types.Message) -> None:
    await message.answer(text=LEXICONE_ALL['email'])


# @dp.message()
# async def test_middleware(message: types.Message) -> None:
#     await message.answer("test_middleware ok!")


# @dp.message(F.content_type.in_({'text'}), lambda message: len(message.text.split(' ')) == 2)
async def filters_two_words(message: types.Message) -> None:
    await message.answer(text=LEXICONE_ALL['two_words'])


# # @dp.message(F.content_type.in_({'text'}), lambda message: "15" in message.text)
async def filters_15(message: types.Message) -> None:
    await message.answer(text=LEXICONE_ALL['filter_15'])


# # @dp.message(F.content_type.in_({'photo'}))
async def photo_echo(message: types.Message) -> None:
    await message.answer(text=LEXICONE_ALL['photo'])
    await message.answer_photo(photo=message.photo[2].file_id)


# @dp.message(Command(commands='close'))
async def close_keyboard(message: types.Message) -> None:
    await message.answer(text=LEXICONE_ALL['close'], reply_markup=types.ReplyKeyboardRemove())


# @dp.message(Command(commands='help'))
async def press_help(message: types.Message) -> None:
    await message.answer(text=LEXICONE_ALL['help'])


# @dp.message(F.content_type.in_({'sticker'}))
async def memory_sticer_id(message: Message):
    await message.answer(text=message.sticker.file_id)
    sticker_id = str(message.sticker.file_id)
    stic_dict.update({'sticker_id': sticker_id})
    return stic_dict


# @dp.message(Command(commands='get_sticker'))
async def get_sticker(message: types.Message) -> None:
    await message.answer_sticker(sticker=stic_dict['sticker_id'])


async def get_inline(message: types.Message) -> None:
    await message.answer(text=LEXICONE_ALL['new_inl_kb'], reply_markup=inl_kb)


async def new_inline_keyboard(message: types.Message) -> None:
    await close_keyboard(message)
    await get_inline(message)


def register_user_handlers(dp: Dispatcher) -> None:
    dp.message.register(start_process, Command(commands='start'))
    dp.message.register(check_emile, EmailFilter())
    dp.message.register(filters_two_words, TwoWords())
    dp.message.register(filters_15, InText15())
    dp.message.register(photo_echo, F.content_type.in_({'photo'}))
    dp.message.register(close_keyboard, Command(commands='close'))
    dp.message.register(press_help, Command(commands='help'))
    dp.message.register(memory_sticer_id, F.content_type.in_({'sticker'}))
    dp.message.register(get_sticker, Command(commands='get_sticker'))
    dp.message.register(new_inline_keyboard, Command(commands='new_inline_keyboard'))
    dp.message.register(get_inline, Command(commands='get_inline'))
