from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pedido
# Create your views here.

@login_required
def index(request):
    pedidos = Pedido.objects.all()
    countProducao = 0
    countConcluido = 0

    CountPedidos = len(pedidos)
    for i in range (CountPedidos):
        if pedidos[i].status == "PRODUCAO":
            countProducao+=1
            CountPedidos-=1
        elif pedidos[i].status == "CONCLUIDO":
            countConcluido+=1
            CountPedidos-=1

    return render(request, "index.html", {"pedidos": pedidos, "CountPedidos": CountPedidos, "CountProducao": countProducao, "CountConcluido": countConcluido } )

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
    salvadescricao = request.POST.get("descricao")
    salvanumero = request.POST.get("numero")
    salvanumeroMesa = request.POST.get("numeroMesa")
    salvaImagem = request.POST.get("imagem")
    Pedido.objects.create(descricao=salvadescricao, numero=salvanumero, numeroMesa=salvanumeroMesa,imagem=salvaImagem)
    return redirect(orders)

def editar(request, id):
    pedido = Pedido.objects.get(id=id)
    data = {}
    data['pedido'] = pedido
    return render(request, "orders/edit.html", data)

def update(request, id):
    salvadescricao = request.POST.get("descricao")
    salvanumero = request.POST.get("numero")
    salvanumeroMesa = request.POST.get("numeroMesa")
    salvaImagem = request.POST.get("imagem")
    pedido = Pedido.objects.get(id=id)
    pedido.descricao = salvadescricao
    pedido.numero = salvanumero
    pedido.numeroMesa = salvanumeroMesa
    pedido.imagem = salvaImagem
    pedido.save()
    return redirect(orders)

def remover(request, id):
    pedido = Pedido.objects.get(id=id)
    pedido.delete()

    if pedido.status == "CONCLUIDO":
        return redirect(index)

    return redirect(orders)

def status(request, id):
   pedido = Pedido.objects.get(id=id)

   if pedido.status == "AGUARDANDO":
    pedido.status = "PRODUCAO"
    pedido.save()

   else:
    pedido.status = "CONCLUIDO"
    pedido.save()
    
   
   return redirect(index)


