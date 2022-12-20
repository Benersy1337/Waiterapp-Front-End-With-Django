from django.contrib import admin
from django.urls import path, include
from .views import index, salvar, editar, update, remover,details, orders, create

urlpatterns = [
    #name=index para poder puxar no LOGIN_REDIRECT_URL em settings.py
    path('', index, name='index'),
    path('all/', orders),
    path('create/', create),
    path('details/', details),
    path('salvar/', salvar, name="salvar"),
    path('editar/<int:id>', editar, name="editar"),
    path('update/<int:id>', update, name="update"),
    path('remover/<int:id>', remover, name="remover"),
]