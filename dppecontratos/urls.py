from django.urls import path
from . import views
from dppecontratos.views import custom_logout 

urlpatterns = [
    path('', views.dppecontratosList, name='dppecontratos-list'),
    path('contratos/tipo/0/', views.contratos_tipo_0, name='contratos-tipo-0'),
    path('contratos/tipo/1/', views.contratos_tipo_1, name='contratos-tipo-1'),
    path('contratos/tipo/2/', views.contratos_tipo_2, name='contratos-tipo-2'),
    path('contratos/delete/<int:id>/', views.deletecontratos, name='delete-contratos'),
    path('contratos/<int:id>', views.contratoView, name='contrato-view'),
    path('newcontratos/', views.newcontratos, name="new-contratos"),
    path('editcontratos/<int:id>/', views.editcontratos, name="edit-contratos"),
    path('accounts/logout/', custom_logout, name='logout'),
    
   
]
