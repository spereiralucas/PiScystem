from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Afericao
from .form import AfericaoForm
import datetime


def home(request):
    data = {}
    data['afericoes'] = ['t1', 't2', 't3']

    data['now'] = datetime.datetime.now()
    # html = "<html><body>Agora são %s horas.</body></html>" % now
    return render(request, 'gerenciamento/home.html', data)


def relatorio(request):
    data = {}
    data['afericoes'] = Afericao.objects.all()
    return render(request, 'gerenciamento/relatorio.html', data)


def nova_afericao(request):
    data = {}
    form = AfericaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_relatorio')

    data['form'] = form
    return render(request, 'gerenciamento/form.html', data)


def editar_afericao(request, pk):
    data = {}
    afericao = Afericao.objects.get(pk=pk)
    form = AfericaoForm(request.POST or None, instance=afericao)

    if form.is_valid():
        form.save()
        return redirect('url_relatorio')

    data['form'] = form
    return render(request, 'gerenciamento/form.html', data)


def excluir_afericao(request, pk):
    afericao = Afericao.objects.get(pk=pk)
    afericao.delete()
    return redirect('url_relatorio')


def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('url_relatorio')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'usuarios/form_usuario.html', {"form_usuario": form_usuario})


def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('url_relatorio')
        else:
            messages.error(request, 'Login e/ou senha incorreto(s)')
            return redirect('logar_usuario')
    form_login = AuthenticationForm()
    return render(request, 'usuarios/login.html', {"form_login": form_login})


def calculo_racao_diaria(afericao):
    pass

