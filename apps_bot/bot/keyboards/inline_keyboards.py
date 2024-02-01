

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from apps_bot.bot.LEXICONES.LEXICON import LEXICON_INLINE_MENU, LEXICON_callback_data, LEXICON_URLS

ib1 = InlineKeyboardButton(text=LEXICON_INLINE_MENU['b1'], callback_data=LEXICON_callback_data['b1'])
ib2 = InlineKeyboardButton(text=LEXICON_INLINE_MENU['b2'], callback_data=LEXICON_callback_data['b2'])
ib3 = InlineKeyboardButton(text=LEXICON_INLINE_MENU['b3'], callback_data=LEXICON_callback_data['b3'])
ib4 = InlineKeyboardButton(text=LEXICON_INLINE_MENU['google'], url=LEXICON_URLS['google'])


inl_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [ib4],
        [ib1, ib2],
        [ib3],
    ])



