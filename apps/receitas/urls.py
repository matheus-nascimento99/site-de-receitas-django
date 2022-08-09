from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/receita', receita, name='receita'),
    path('busca', busca, name='buscar'),
    path('cria/receita', cria_receita, name='cria_receita'),
    path('deleta/<int:id>', deleta_receita, name='deleta_receita'),
    path('edita/<int:id>', edita_receita, name='edita_receita'),
]