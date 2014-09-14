from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'django.contrib.auth.views.login',
    #     {'template_name': 'login.html', 'authentication_form': LoginForm},
    #     name='entrar'),
    url(r'^$', 'pbd.accounts.views.entrar', name='entrar'),

    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': 'login:entrar'}, name='sair'),

    #url(r'^home/$', 'Absistema.core.views.home', name='home'),
)
