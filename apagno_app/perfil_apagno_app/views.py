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
            nombre = request.POST['nombre']#.get('nombre',False)
            host = request.POST.get('host','default value')
            lugar = request.POST['lugar']#.get('lugar',False)
            descripcion = request.POST['descripcion']#.get('descripcion',False)
            categoria = Categorias.objects.get(nombre=request.POST["selector_categoria"])
            imagen = request.FILES.get('imagen',False)
            nuevo_evento = nuevoEvento(nombre=nombre, host=host, lugar=lugar, descripcion=descripcion, categoria=categoria, imagen=imagen)
            nuevo_evento.save()
            return redirect('/perfil_apagno_app/crear_evento')
