# Generated by Django 5.0.6 on 2024-05-22 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dppecontratos', '0004_rename_obejto_contrato_objeto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='cnpj_cpf',
            field=models.CharField(max_length=14),
        ),
    ]
