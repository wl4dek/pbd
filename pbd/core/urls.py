from django.conf.urls import patterns, url


urlpatterns = patterns(
    'pbd.core.views',
    url(r'^$', 'home', name='home'),
)
