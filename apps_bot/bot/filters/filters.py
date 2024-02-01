import re  # регулярные выражения
from typing import Match, Any, Coroutine

from aiogram import types, F
from aiogram.filters import Filter


class EmailFilter(Filter):
    key = 'is_emaile'

    # регулярное выражение (любые символы)@(любые символы).(либо com либо ua)
    pattern = re.compile(r'[\w.-]+@[\w-]+\.(com|ua)')

    async def check(self, message: types.Message) -> bool:
        if message.text:
            return self.pattern.match(message.text) is not None

    def __call__(self, message: types.Message) -> Coroutine[Any, Any, bool]:
        return self.check(message)


# (F.content_type.in_({'text'}), lambda message: len(message.text.split(' '))==2)
class TwoWords(Filter):
    key = 'is_two_words'

    async def two_words(self, message: types.Message) -> bool:
        if message.text:
            len_message_text = len(message.text.split(' '))
            if len_message_text == 2:
                return True
        else:
            return False

    def __call__(self, message: types.Message) -> Coroutine[Any, Any, bool]:
        return self.two_words(message)


# (F.content_type.in_({'text'}), lambda message: "15" in message.text)
class InText15(Filter):
    key = 'in_text_message_15'

    async def in_text_message_15(self, message: types.Message) -> bool:
        if message.text:
            if "15" in message.text:
                return True
        else:
            return False

    def __call__(self, message: types.Message) -> Coroutine[Any, Any, bool]:
        return self.in_text_message_15(message)

