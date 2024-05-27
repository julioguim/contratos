from django.contrib import admin
from .models import Contrato

class ContratoAdmin(admin.ModelAdmin):
    list_display = ('num_contrato', 'num_ata', 'fornecedor', 'cnpj_cpf', 'ano', 'modalidade', 'valor_mensal', 'valor_anual', 'inicio_vigencia', 'final_vigencia', 'status_display', 'fiscal', 'data_vencimento', 'data_pagamento', 'tipo')
    search_fields = ('num_contrato', 'num_ata', 'fornecedor', 'cnpj_cpf')
    list_filter = ('ano', 'modalidade', 'inicio_vigencia', 'final_vigencia', 'done', 'tipo')
    
    def status_display(self, obj):
        return obj.get_done_display()
    status_display.short_description = 'Status'

admin.site.register(Contrato, ContratoAdmin)
