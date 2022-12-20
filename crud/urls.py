from django.contrib import admin
from django.urls import path, include
from .views import index, salvar, editar, update, remover,details, orders, create

urlpatterns = [
    path('', index),
    path('orders/', orders),
    path('orders/create/', create),
    path('details/', details),
    path('orders/salvar/', salvar, name="salvar"),
    path('editar/<int:id>', editar, name="editar"),
    path('update/<int:id>', update, name="update"),
    path('remover/<int:id>', remover, name="remover"),
]