from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from apps_bot.bot.LEXICONES.LEXICON import LEXICON_MAIN_MENU

b1 = KeyboardButton(text=LEXICON_MAIN_MENU['btn_sticker'])
b2 = KeyboardButton(text=LEXICON_MAIN_MENU['btn_help'])
b3 = KeyboardButton(text=LEXICON_MAIN_MENU['btn_phone'], request_contact=True)
b4 = KeyboardButton(text=LEXICON_MAIN_MENU['btn_inl_kb'])
b_close = KeyboardButton(text=LEXICON_MAIN_MENU['btn_close'])

kb_client = ReplyKeyboardMarkup(
    keyboard=[
        [b1, b2],
        [b3],
        [b4],
        [b_close]
    ]
)





