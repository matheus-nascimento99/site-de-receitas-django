from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Receita
# Create your views here.

def index(request):
    receitas = Receita.objects.all()

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
