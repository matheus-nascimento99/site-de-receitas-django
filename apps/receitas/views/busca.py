from django.shortcuts import get_object_or_404, render, get_list_or_404,redirect
from ..models import Receita

def busca(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if (busca):
            receitas = receitas.filter(nome_receita__icontains=nome_a_buscar)
            
    dados = {
        'receitas':receitas
    }

    return render(request, 'receitas/buscar.html', dados)