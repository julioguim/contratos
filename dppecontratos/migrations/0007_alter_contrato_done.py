# Generated by Django 5.0.6 on 2024-05-22 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dppecontratos', '0006_alter_contrato_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='done',
            field=models.IntegerField(choices=[(0, 'vigente'), (1, 'Encerrado')]),
        ),
    ]
