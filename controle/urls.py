"""controle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gerenciamento.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relatorio/', relatorio, name='url_relatorio'),
    path('', home, name='url_inicio'),
    path('nova-afericao/', nova_afericao, name='url_nova-afericao'),
    path('editar_afericao/<int:pk>/', editar_afericao, name='url_editar_afericao'),
    path('excluir_afericao/<int:pk>/', excluir_afericao, name='url_excluir_afericao'),
    path('cadastrar_usuario/', cadastrar_usuario, name='url_cadastrar_usuario'),
    path('login/', logar_usuario, name='url_logar_usuario'),
]
