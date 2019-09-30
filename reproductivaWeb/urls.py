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
from django.conf.urls.static import static
from reproductivaApp import views
from reproductivaWeb import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.main, name="main"),
    url(r'^base/$', views.base, name="base"),
    url(r'^el_proyecto/$', views.nosotros, name="el_proyecto"),
    url(r'^nuestro_equipo/$', views.nuestro_equipo, name="nuestro_equipo"),

    url('^politica/$', views.politica_privacidad, name='politica'),
    url('^blog/$', views.blog, name='blog'),
    url('^post/$', views.postContenido, name='post'),
    url('^videos/$', views.videos, name='videos'),

    url('^directorio/$', views.lista_centros_medicos, name='directorio'),
    url('^directorio/$', views.lista_centros_medicos, name='directorio'),
    url(r'^email/$', views.contacto.as_view(), name="email"),

    url(r'^detalle_post/$', views.postDetalle, name="detalle_post"),
]
# SI EL DEBUG ES TRUE ENTONCES QUE TOME LA CARPETA STATIC_URL, DE LO CONTRARIO QUE UTILIZE LA CARPETA MEDIA_URL
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)