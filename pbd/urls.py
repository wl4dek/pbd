from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('pbd.accounts.urls', namespace='login')),
    url(r'^home/', include('pbd.core.urls', namespace='core')),
    url(r'^funcionario/', include('pbd.funcionario.urls', namespace='funcionario')),
    url(r'^cliente/', include('pbd.cliente.urls', namespace='cliente')),
    url(r'^contrato/', include('pbd.contrato.urls', namespace='contrato')),
    url(r'^manutencao/', include('pbd.manutencao.urls', namespace='manutencao')),
    url(r'^produto/', include('pbd.produto.urls', namespace='produto')),
)
