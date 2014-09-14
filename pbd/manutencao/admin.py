from django.contrib import admin
from .models import Manuntencao


class ManuntencaoAdmin(admin.ModelAdmin):
    list_display = ['produto', 'data', 'valor_gasto']
    search_fields = ['produto']

admin.site.register(Manuntencao, ManuntencaoAdmin)
