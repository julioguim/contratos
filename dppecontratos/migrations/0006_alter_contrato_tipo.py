# Generated by Django 5.0.6 on 2024-05-22 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dppecontratos', '0005_alter_contrato_cnpj_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='tipo',
            field=models.IntegerField(choices=[(0, 'Atas de Registro de Preço'), (1, 'Contratos de Locação de Imóveis'), (2, 'Demais Contratos')]),
        ),
    ]
