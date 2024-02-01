import logging
from pprint import pprint

from aiogram import Dispatcher, F
from aiogram.types import CallbackQuery

from apps_bot.bot.LEXICONES.LEXICON import LEXICONE_ALL, LEXICON_callback_data

logger = logging.getLogger(__name__)


async def press_btn_3_inl(call: CallbackQuery) -> None:
    await call.message.answer(text=LEXICONE_ALL['btn_3_inl'])
    await call.answer()
    logger.info(f'press btn_3_inl {call.message.chat.username} - {call.data}')


async def press_inl_1_2_btn(call: CallbackQuery) -> None:
    data = call.data.rsplit("_")
    if int(data[2]) == 1:
        await call.message.answer(text='нажал на кнопку 1')
        await call.answer()
    elif int(data[2]) == 2:
        await call.message.answer(text='нажал на кнопку 2')
        await call.answer()
    logger.info(f'press btn_3_inl {call.message.chat.username} -  {call.data}')


def register_callback_handlers(dp: Dispatcher) -> None:
    dp.callback_query.register(press_inl_1_2_btn, F.data.startswith('inl'))
    dp.callback_query.register(press_btn_3_inl, F.data.contains(LEXICON_callback_data["b3"]))
