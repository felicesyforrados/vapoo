
# -*- coding: utf-8 -*-
from django.conf.urls import url
from home.views import carro, carro_final

urlpatterns = [
    url(r'^carro/$', carro, name='carro'),
    url(r'^carro/final/$', carro_final, name='carro_final'),
]
