import re
from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Receita
# Create your views here.

def index(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    dados = {
        'receitas': receitas
    }

    return render(request, 'index.html', dados)

def receita(request, pk):

    receita = get_object_or_404(Receita, pk=pk)

    context= {
        'receita': receita
    }
    
    return render(request, 'receita.html', context)

def buscar(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if (buscar):
            receitas = receitas.filter(nome_receita__icontains=nome_a_buscar)
            
    dados = {
        'receitas':receitas
    }

    return render(request, 'buscar.html', dados)