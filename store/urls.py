from django.urls import path

from store.apps import StoreConfig
from store.views import items_list, items_detail, buy

app_name = StoreConfig.name

urlpatterns = [
    path('', items_list, name='items_list'), # Главная страница со всеми товарами
    path('item/<int:pk>/', items_detail, name='items_detail'), #Детальная информация о товаре
    path('buy/<int:pk>/', buy, name='buy') #Путь запускающий скрипт для оплаты
]