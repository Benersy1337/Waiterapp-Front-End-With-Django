# Generated by Django 4.1.5 on 2023-01-12 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0009_alter_pedido_numeromesa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='numeroMesa',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
