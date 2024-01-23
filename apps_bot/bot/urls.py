from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start, name='start'),
    # Добавьте другие маршруты по мере необходимости
]