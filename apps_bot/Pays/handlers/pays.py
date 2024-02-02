from aiogram import F

from aiogram import Bot, Dispatcher

from aiogram.filters import Command

from aiogram.types import Message, LabeledPrice, PreCheckoutQuery

from Config.settings import Portmone_TOKEN



async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Покупка без доставки',
        description='учимся принимать платежи',
        payload='внутренняя переменная, можно записать статистику',
        provider_token=Portmone_TOKEN,
        currency='UAH',
        prices=[
            LabeledPrice(
                label='tovar1',
                amount=10000  # цена в копейках
            ),
            LabeledPrice(
                label='НДС',
                amount=2000  # цена в копейках
            ),
            LabeledPrice(
                label='скидка',
                amount=1000  # цена в копейках
            ),
            LabeledPrice(
                label='бонус',
                amount=500  # цена в копейках
            ),
            LabeledPrice(
                label='tovar1',
                amount=10000  # цена в копейках
            )
        ],
        max_tip_amount=10000,  # максимальная сумма чаевых
        suggested_tip_amounts=[1000, 2000, 5000, 9999],  # спсиок возможных чаевых
        start_parameter="qwerty",  # дает возможность отправить ссылку на оплату в другой чат
        provider_data=None,
        photo_url="https://play-lh.googleusercontent.com/Z3NrTj77K_ieQshGlYjDByml-ogzuf6Uki6uLQ7MzVN7i1byDaE2j-QlCAEzaGA4KZI=w526-h296-rw",
        photo_size=100,
        photo_width=800,
        photo_height=450,
        need_name=True,  # запросить данные у покупателя
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        send_phone_number_to_provider=False,  # Передать данные для провайдера
        send_email_to_provider=False,
        is_flexible=False,  # Зависит ли цена отдоставки
        disable_notification=False,  # Доставить сообщение без звука
        protect_content=False,  # Защитить пост от копирования или пересылки
        reply_to_message_id=None,  # id для того чтобы процетировать сообщение
        allow_sending_without_reply=True,  # Отправить счет на оплату даже если цитируемое сообщение не найдено
        reply_markup=None,  # Добавить клавиатуру, первая кнопка должна быть оплатить
        request_timeout=15  # таймаут запроса
    )


# ответ на предварительный запрос что данные получены и товар готов к отправке
async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    # тут проверяем возможно ли сейчас отправить товар, наличие и так дальше (ok=True/ok=False)
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: Message):
    msg = f"Спасибо за оплату {message.successful_payment.total_amount // 100} " \
          f"{message.successful_payment.currency}." \
          f"\r\nНаш менеджер проверит данные и свяжется с вами"
    "\r\nСсылка на ваш товар:"
    f"\r\nhttps://play-lh.googleusercontent.com/fN5OJYzbt7-TTEWkC07EvWdrtO4PNgmAhjMcXEbuN_vl0WSAlxb-lCvy89upxGy8sw=w2560-h1440-rw"

    await message.answer(msg)





def register_pays_handlers(dp: Dispatcher) -> None:
    dp.message.register(order, Command(commands='pay'))
    dp.pre_checkout_query.register(pre_checkout_query)
    dp.message.register(successful_payment, F.successful_payment)
