from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pedido
# Create your views here.

@login_required
def index(request):
    return render(request, "index.html")

@login_required
def orders(request):
    pedidos = Pedido.objects.all()
    return render(request, "orders/all.html", {"pedidos": pedidos})

@login_required
def details(request, id):
    pedido = Pedido.objects.get(id=id)
    data = {}
    data['pedido'] = pedido
    return render(request, "orders/detail.html", data)
    

def criando(request):
    return render(request, "orders/create.html")

def create(request):
    salvanome = request.POST.get("nome")
    Pedido.objects.create(nome=salvanome)
    return redirect(orders)

def editar(request, id):
    pedido = Pedido.objects.get(id=id)
    data = {}
    data['pedido'] = pedido
    return render(request, "orders/edit.html", data)

def update(request, id):
    salvanome = request.POST.get("nome")
    pedido = Pedido.objects.get(id=id)
    pedido.nome = salvanome
    pedido.save()
    return redirect(orders)

def remover(request, id):
    pedido = Pedido.objects.get(id=id)
    pedido.delete()
    return redirect(orders)

