from django.forms import ModelForm
from .models import Afericao, Tanque, Categoria


class AfericaoForm(ModelForm):
    class Meta:
        model = Afericao
        fields = ['id', 'quantidade', 'peso', 'categoria', 'observacoes']


"""class TanqueForm(ModelForm):
    class Meta:
        model = Tanque
        fields = ['id', 'categoria', 'observacoes']


    class Categoria(ModelForm): ESTÁ DANDO BUG (CORRIGIR)
    class Meta:
        model = Categoria
        fields = ['nome', 'data_criacao']"""
