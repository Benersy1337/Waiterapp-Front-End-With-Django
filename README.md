Passo a Passo

Request (request)
views.py -> def salvar(request):

Acha a URL (salvar/)
path('salvar/', salvar, name="salvar"),

procura a VIEW da URL (salvar)
urls.py -> path('salvar/', salvar, name="salvar") // salvar é a view

Na view manipula os models (Pessoa.objects.create(nome=salvanome) e pessoas = Pessoa.objects.all())
def salvar(request):
    salvanome = request.POST.get("nome")
    Pessoa.objects.create(nome=salvanome)
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

