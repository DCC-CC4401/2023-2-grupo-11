from django.shortcuts import render, redirect
from django.http import HttpResponse
from perfil_apagno_app.forms import NuevoEventoForm
from perfil_apagno_app.models import *


# Create your views here.

def initPerfil(request):
    return HttpResponse("Pagina de Perfil de usuario")

def creacionEvento(request):
    mis_eventos = nuevoEvento.objects.all()
    categorias = Categorias.objects.all()
    #context = {}
    #context['form'] = NuevoEventoForm()

    if request.method == "GET":
       #form = NuevoEventoForm()
        return render(request, 'perfil_app/creacionEvento.html', {"eventos": mis_eventos, "categorias": categorias})
    
    if request.method == "POST":
        if "eventAdd" in request.POST:
            nombre = request.POST["nombre"]
            host = request.POST["host"]
            lugar = request.POST["lugar"]
            descripcion = request.POST["descripcion"]
            categoria = Categorias.objects.get(nombre=request.POST["selector_categoria"])
            nuevo_evento = nuevoEvento(nombre=nombre, host=host, lugar=lugar, descripcion=descripcion, categoria=categoria)
            nuevo_evento.save()
            return redirect('/perfil/crear_evento')
