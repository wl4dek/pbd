from django.conf.urls import patterns, url


urlpatterns = patterns(
    'pbd.manutencao.views',
    url(r'cadastrar$', 'cadastrar', name='cadastrar'),
)
