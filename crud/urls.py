from django.contrib import admin
from django.urls import path, include
from .views import home, salvar, editar, update, remover,list

urlpatterns = [
    path('', home),
    path('list/', list),
    path('salvar/', salvar, name="salvar"),
    path('editar/<int:id>', editar, name="editar"),
    path('update/<int:id>', update, name="update"),
    path('remover/<int:id>', remover, name="remover"),
]