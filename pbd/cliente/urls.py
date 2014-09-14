from django.conf.urls import patterns, url


urlpatterns = patterns(
    'pbd.cliente.views',
    url(r'cadastrar$', 'cadastrar', name='cadastrar'),
    url(r'listar$', 'listar', name='listar'),
    url(r'^editar/(?P<pk>\d+)$', 'editar', name='editar'),
)
