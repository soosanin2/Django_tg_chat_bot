from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bot/', include('apps_bot.bot.urls')),  # Добавили URL-пути для бота
    # Добавь другие URL-пути, если необходимо
]