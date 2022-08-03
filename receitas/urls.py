from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/receita', views.receita, name='receita'),
    path('buscar', views.buscar, name='buscar')
]