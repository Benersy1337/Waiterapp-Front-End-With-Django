# Generated by Django 4.1.5 on 2023-01-05 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_pedido_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='descricao',
            field=models.CharField(max_length=30, null=True),
        ),
    ]