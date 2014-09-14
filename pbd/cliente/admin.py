from django.contrib import admin
from .models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'cnpj']
    search_fields = ['username']

admin.site.register(Cliente, ClienteAdmin)
