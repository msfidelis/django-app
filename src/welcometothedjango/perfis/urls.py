# -*- coding: UTF-8 -*-

from django.conf.urls import url

from perfis.views import index, exibir, convidar

##
# Rotas do modulo de Perfis
##
urlpatterns = [
    
    ##
    # Login
    ##

    ##
    # Perfis
    ##
    url(r'^$', index, name='index'),
    url(r'^perfil/(?P<perfil_id>\d+)$', exibir, name='exibir'),
    url(r'^perfil/(?P<perfil_id>\d+)/convidar$', convidar, name='convidar'),
]
