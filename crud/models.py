from django.db import models

# Create your models here.

class Pedido(models.Model):

    nome = models.CharField(max_length=30)

    numero = models.IntegerField(default=None)

    numeroMesa = models.IntegerField(default=None)

    def __str__(self):
        return self.nome