from django.db import models

# Create your models here.

class Pedido(models.Model):

    STATUS_AGUARDANDO = "AGUARDANDO"
    STATUS_PRODUCAO = "PRODUCAO"
    STATUS_CONCLUIDO = "CONCLUIDO"


    STATUSPEDIDOS_CHOICES = [
        (STATUS_AGUARDANDO, "Aguardando"),
        (STATUS_PRODUCAO, "Em Produção"),
        (STATUS_CONCLUIDO, "Concluído"),

    ]

    descricao = models.CharField(max_length=30, null=True)

    numero = models.IntegerField(null=True, default=None)

    numeroMesa = models.IntegerField(null=True, default=None)

    imagem = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default=None)

    status = models.CharField(max_length=10, choices=STATUSPEDIDOS_CHOICES, default= STATUS_AGUARDANDO)

    def __str__(self):
        return self.descricao