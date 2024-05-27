from django import forms
from .models import Contrato

class ContratoForm(forms.ModelForm):
   
    class Meta:
        model = Contrato
        fields = [
            'ano',
            'tipo',
            'fiscal',
            'num_ata',
            'cnpj_cpf',
            'modalidade',
            'valor_anual',
            'valor_mensal',
            'num_contrato',
            'num_modalidade',
            'num_processos_licitatorio',
            'fornecedor',
            'objeto',
            'inicio_vigencia',
            'final_vigencia',
            'data_vencimento',
            'data_pagamento',
            'done',
        ]
        widgets = {
            'inicio_vigencia': forms.DateInput(attrs={'type': 'date'}),
            'final_vigencia': forms.DateInput(attrs={'type': 'date'}),
            'data_vencimento': forms.DateInput(attrs={'type': 'date'}),
            'data_pagamento': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            if self.instance.inicio_vigencia:
                self.initial['inicio_vigencia'] = self.instance.inicio_vigencia.strftime('%Y-%m-%d')
            if self.instance.final_vigencia:
                self.initial['final_vigencia'] = self.instance.final_vigencia.strftime('%Y-%m-%d')
            if self.instance.data_vencimento:
                self.initial['data_vencimento'] = self.instance.data_vencimento.strftime('%Y-%m-%d')
            if self.instance.data_pagamento:
                self.initial['data_pagamento'] = self.instance.data_pagamento.strftime('%Y-%m-%d')
