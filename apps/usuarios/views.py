from operator import truediv
import re
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita
# Create your views here.

def cadastro(request):

    if request.method == 'POST':
        
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if campo_vazio(nome):
            messages.error(request, 'Preencha o campo de nome.')
            return redirect('cadastro')

        if campo_vazio(email):
            messages.error(request, 'Preencha o campo de email.')
            return redirect('cadastro')

        if verifica_equidade_senha(senha,senha2):
            messages.error(request, 'As senhas não são iguais.')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists() and User.objects.filter(username=nome).exists():
            messages.error(request, 'Este usuário já existe.')
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()

        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login')
    else:    
        return render(request, 'usuarios/cadastro.html')

def login(request):

    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Preencha todos os campos.')
            return redirect('login')
        
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username = nome, password=senha)
            
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Email e/ou senha inválidos.')
                return redirect('login')

    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=id)
        dados = {
            'receitas':receitas
        }
        
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def campo_vazio(campo):
    return not campo.strip()

def verifica_equidade_senha(senha1, senha2):
    return senha1 != senha2