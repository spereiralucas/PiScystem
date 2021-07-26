from django.contrib import admin  # Importa a função de administrador pro sistema via browser
from .models import *  # Importa tabelas do models

admin.site.register(Categoria)  # Adiciona a criação da tabela no módulo do administrador
admin.site.register(Afericao)
admin.site.register(Tanque)

# Register your models here.
