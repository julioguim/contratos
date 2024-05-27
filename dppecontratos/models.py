from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Contrato(models.Model):


    tipo_contrato = (

        (0,'Atas de Registro de Preço'),
        (1,'Contratos de Locação de Imóveis'),
        (2,'Demais Contratos')
    )
 
    STATUS = (
        (0,'vigente'),
        (1,'Encerrado')
    )
    ano = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2100)])
    num_contrato = models.CharField(max_length=50)
    num_ata = models.CharField(max_length=50)
    num_processos_licitatorio = models.CharField(max_length=150)
    modalidade = models.CharField(max_length=50)
    num_modalidade = models.CharField(max_length=150)
    objeto = models.TextField()
    fornecedor = models.TextField()
    cnpj_cpf = models.CharField(max_length=14)
    valor_mensal = models.CharField(max_length=50)
    valor_anual = models.CharField(max_length=50)
    inicio_vigencia = models.DateField()
    final_vigencia = models.DateField()
    done = models.IntegerField(
        
        choices= STATUS,
    )
    fiscal = models.CharField(max_length=50)
    data_vencimento = models.DateField()
    data_pagamento = models.DateField()
    tipo = models.IntegerField(

        choices = tipo_contrato,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.num_contrato