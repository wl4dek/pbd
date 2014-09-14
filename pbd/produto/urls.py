from django.conf.urls import patterns, url


urlpatterns = patterns(
    'pbd.produto.views',
    url(r'cadastrar$', 'cadastrar', name='cadastrar'),
)
