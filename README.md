# Django_tg_chat_bot

1. Клонируем проэкт к себе

2. Устанавливаем небходимые биб-ки `pip install -r requirements.txt`

3. Поготовка к запуску

    * Проводим миграции `make makemigrations`

    * Готовим среду:

    - Сначала нжно запустит ngrock на ubuntu:
        - запускаем ubuntu,
        - прверяем запужен ли ngrock `sudo service redis-server status`
    - Заполняем свой `.env`

4. Запуск бота `manage.py run_bot`
