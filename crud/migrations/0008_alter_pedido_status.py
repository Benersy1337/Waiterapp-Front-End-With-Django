# Generated by Django 4.1.5 on 2023-01-09 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0007_alter_pedido_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('AGUARDANDO', 'Aguardando'), ('PRODUCAO', 'Em Produção'), ('CONCLUIDO', 'Concluído')], default='AGUARDANDO', max_length=10),
        ),
    ]