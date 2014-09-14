from django.contrib import admin
from .models import Produto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'quantidade', 'date_joined']
    search_fields = ['nome']

admin.site.register(Produto, ProdutoAdmin)
