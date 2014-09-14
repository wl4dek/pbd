from django.conf.urls import patterns, url


urlpatterns = patterns(
    'pbd.contrato.views',
    url(r'cadastrar$', 'cadastrar', name='cadastrar'),
)
