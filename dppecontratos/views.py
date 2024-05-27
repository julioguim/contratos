from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import ContratoForm
from .models import Contrato
from django.contrib.auth import logout



@login_required
def custom_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dppecontratosList(request):
    dppecontratos_list = Contrato.objects.all().order_by('-ano')

    search_query = request.GET.get('search')
    if search_query:
        dppecontratos_list = dppecontratos_list.filter(
            Q(num_contrato__icontains=search_query) |                   
            Q(num_ata__icontains=search_query) |                       
            Q(num_processos_licitatorio__icontains=search_query) |   
            Q(modalidade__icontains=search_query) |                   
            Q(objeto__icontains=search_query) |                       
            Q(fornecedor__icontains=search_query) |                   
            Q(cnpj_cpf__icontains=search_query) |                   
            Q(fiscal__icontains=search_query)                     
        )

    paginator = Paginator(dppecontratos_list, 5) 
    page = request.GET.get('page')
    dppecontratos = paginator.get_page(page)  

    return render(request, 'dppecontratos/list.html', {'dppecontratos': dppecontratos, 'search_query': search_query})
@login_required
def contratos_tipo_0(request):
    contratos = Contrato.objects.filter(tipo=0)
    return render(request, 'dppecontratos/contratos_tipo_0.html', {'contratos': contratos, 'tipo': 'Tipo 0'})
@login_required
def contratos_tipo_1(request):
    contratos = Contrato.objects.filter(tipo=1)
    return render(request, 'dppecontratos/contratos_tipo_1.html', {'contratos': contratos, 'tipo': 'Tipo 1'})
@login_required
def contratos_tipo_2(request):
    contratos = Contrato.objects.filter(tipo=2)
    return render(request, 'dppecontratos/contratos_tipo_2.html', {'contratos': contratos, 'tipo': 'Tipo 2'})
@login_required
def contratoView(request, id):
    contrato = get_object_or_404(Contrato, pk=id)
    return render(request, 'dppecontratos/contrato.html', {'contrato': contrato})

@login_required
def get_tipo_redirect(tipo):
    if tipo == 0:
        return redirect('contratos-tipo-0')
    elif tipo == 1:
        return redirect('contratos-tipo-1')
    elif tipo == 2:
        return redirect('contratos-tipo-2')
    else:
        return redirect('dppecontratos-list')
@login_required
def newcontratos(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dppecontratos-list')
    else:
        form = ContratoForm()
    return render(request, 'dppecontratos/addcontrato.html', {'form': form})
@login_required
def editcontratos(request, id):
    contrato = get_object_or_404(Contrato, pk=id)
    if request.method == 'POST':
        form = ContratoForm(request.POST, instance=contrato)
        if form.is_valid():
            contrato = form.save()
            return redirect(get_edit_redirect_url(contrato))
    else:
        form = ContratoForm(instance=contrato)
    return render(request, 'dppecontratos/editcontrato.html', {'form': form, 'contrato': contrato})
@login_required
def deletecontratos(request, id):
    contrato = get_object_or_404(Contrato, pk=id)
    if request.method == 'POST':
        tipo_contrato = contrato.tipo
        contrato.delete()
        return redirect(get_delete_redirect_url(tipo_contrato))
    return render(request, 'dppecontratos/deletecontrato.html', {'contrato': contrato})
@login_required
def get_edit_redirect_url(contrato):
    if contrato.tipo == 0:
        return 'contratos-tipo-0'
    elif contrato.tipo == 1:
        return 'contratos-tipo-1'
    elif contrato.tipo == 2:
        return 'contratos-tipo-2'
    else:
        return 'dppecontratos-list'
@login_required
def get_delete_redirect_url(tipo_contrato):
    if tipo_contrato == 0:
        return 'contratos-tipo-0'
    elif tipo_contrato == 1:
        return 'contratos-tipo-1'
    elif tipo_contrato == 2:
        return 'contratos-tipo-2'
    else:
        return 'dppecontratos-list'