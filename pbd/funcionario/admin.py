from django.contrib import admin
from .models import Funcionario


class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['username', 'cpf', 'funcao']
    search_fields = ['username']

admin.site.register(Funcionario, FuncionarioAdmin)
