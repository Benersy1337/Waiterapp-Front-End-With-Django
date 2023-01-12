from django.contrib import admin
from django.urls import path, include
from .views import index, editar, update, remover,details, orders, create, criando, status

urlpatterns = [
    #name=index para poder puxar no LOGIN_REDIRECT_URL em settings.py
    path('', index, name='index'),
    path('all/', orders),
    path('criando/', criando),
    path('create/', create, name="create"),
    path('editar/<int:id>', editar, name="editar"),
    path('update/<int:id>', update, name="update"),
    path('remover/<int:id>', remover),
    path('details/<int:id>', details),
    path('<int:id>', status, name="status")
]