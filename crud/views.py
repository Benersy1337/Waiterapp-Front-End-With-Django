from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pessoa
# Create your views here.


def home(request):
    return render(request, "home/home.html")

@login_required
def list(request):
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def salvar(request):
    salvanome = request.POST.get("nome")
    Pessoa.objects.create(nome=salvanome)
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, "update.html", {"pessoa": pessoa})

def update(request, id):
    salvanome = request.POST.get("nome")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = salvanome
    pessoa.save()
    return redirect(list)

def remover(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)

