from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect



# Create your views here.
from reproductivaApp.form import ContactForm
from reproductivaApp.models import Noticias, PostContenido, Videos


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
    noticias = Noticias.objects.all()
    return render(request,'blog.html',{'noticias':noticias})

def postContenido(request):
    post = PostContenido.objects.all()
    return render(request,'post_contenidos.html',{'post':post})
def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['gallardoerick89@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

def lista_centros_medicos(request):
    return render(request,'directorio_medico.html')

def videos(request):
    videos=Videos.objects.all()
    return render (request,'videos.html',{'videos':videos})