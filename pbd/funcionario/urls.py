from django.conf.urls import patterns, url


urlpatterns = patterns(
    'pbd.funcionario.views',
    url(r'cadastrar$', 'cadastrar', name='cadastrar'),
    url(r'listar$', 'listar', name='listar'),
)
