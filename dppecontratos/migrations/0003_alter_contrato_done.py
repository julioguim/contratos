# Generated by Django 5.0.6 on 2024-05-16 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dppecontratos', '0002_alter_contrato_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='done',
            field=models.IntegerField(choices=[(0, 'vigente'), (1, 'nao vigente ')]),
        ),
    ]
