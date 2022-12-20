from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pedido
# Create your views here.

@login_required
def index(request):
    return render(request, "index.html")

@login_required
def orders(request):
    return render(request, "orders/all.html")

@login_required
def create(request):
    return render(request, "orders/create.html")

@login_required
def details(request):
    pedidos = Pedido.objects.all()
    return render(request, "index.html", {"pedidos": pedidos})

def salvar(request):
    salvanome = request.POST.get("nome")
    Pedido.objects.create(nome=salvanome)
    pedidos = Pedido.objects.all()
    return render(request, "all.html", {"pedidos": pedidos})

def editar(request, id):
    pedido = Pedido.objects.get(id=id)
    return render(request, "update.html", {"pedido": pedido})

def update(request, id):
    salvanome = request.POST.get("nome")
    pedido = Pedido.objects.get(id=id)
    pedido.nome = salvanome
    pedido.save()
    return redirect(details)

def remover(request, id):
    pedido = Pedido.objects.get(id=id)
    pedido.delete()
    return redirect(index)

