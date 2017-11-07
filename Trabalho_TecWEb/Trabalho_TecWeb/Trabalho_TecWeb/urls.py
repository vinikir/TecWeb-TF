"""Trabalho_TecWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core.views import index
from core.views import noticias
from core.views import login
from core.views import graduacao
from core.views import novaDisciplina
from core.views import uploadFoto
from core.views import mostraFoto


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^noticias/$', noticias),
    url(r'^login/$', login),
    url(r'^index/$', index),
    url(r'^graduacao/$', graduacao),
    url(r'^noticias/$', noticias),
    url(r'^novaDisciplina/$', novaDisciplina),
    url(r'^uploadFoto/$', uploadFoto),
    url(r'^mostraFoto/$', mostraFoto),
]
