"""reproductivaWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from reproductivaApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.main, name="main"),
    url(r'^base/$', views.base, name="base"),
    url(r'^el_proyecto/$', views.nosotros, name="el_proyecto"),
    url(r'^nuestro_equipo/$', views.nuestro_equipo, name="nuestro_equipo"),
    url('^email/$', views.emailView, name='email'),
    url('^politica/$', views.politica_privacidad, name='politica'),
    url('^success/$', views.successView, name='success'),
    url('^directorio/$', views.lista_centros_medicos, name='directorio'),
]
