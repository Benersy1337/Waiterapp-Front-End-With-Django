from django.db import models

# Create your models here.

class Pedido(models.Model):

    descricao = models.CharField(max_length=30, null=True)

    numero = models.IntegerField(null=True, default=None)

    numeroMesa = models.IntegerField(null=True, default=None)

    imagem = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default=None)

    def __str__(self):
        return self.descricao