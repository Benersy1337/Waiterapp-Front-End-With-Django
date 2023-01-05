# Generated by Django 4.1.5 on 2023-01-05 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30)),
                ('numero', models.IntegerField(default=None)),
                ('numeroMesa', models.IntegerField(default=None)),
            ],
        ),
        migrations.DeleteModel(
            name='Pessoa',
        ),
    ]
