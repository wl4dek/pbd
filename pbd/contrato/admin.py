from django.contrib import admin
from .models import Contrato


class ContratoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'entrega', 'duracao']
    search_fields = ['cliente']

admin.site.register(Contrato, ContratoAdmin)
