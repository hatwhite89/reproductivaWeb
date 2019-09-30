from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect



# Create your views here.
from django.views import View

from reproductivaApp.form import ContactForm, correo
from reproductivaApp.models import Noticias, PostContenido, Videos,Post


def main(request):
    lista_noticias= Noticias.objects.all()
    return render(request, 'index.html',{'lista_noticias':lista_noticias})

def base(request):
    return render(request, 'base.html')

def nosotros(request):
    return render(request,'quienes_somos.html')

def nuestro_equipo(request):
    return render(request,'nuestro_quipo.html')
def politica_privacidad(request):
    return render(request,'politicas_privacidad.html')

def blog(request):
    noticias = Post.objects.all()
    return render(request,'blog.html',{'noticias':noticias})

def postContenido(request):
    post = PostContenido.objects.all()
    return render(request,'post_contenidos.html',{'post':post})
def postDetalle(request):
    id_post= request.GET['id_post']
    detalle_post=PostContenido.objects.filter(pk=id_post)
    return  render(request,'detalle_post.html',{'detalle_post':detalle_post})


def lista_centros_medicos(request):
    return render(request,'directorio_medico.html')

def videos(request):
    videos=Videos.objects.all()
    return render (request,'videos.html',{'videos':videos})

class contacto(View):
    def get(self,request):
        form=correo()
        return render(request,'contacto.html',{'forma':form})