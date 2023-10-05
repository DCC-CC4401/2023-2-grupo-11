from django.shortcuts import render, redirect
from django.http import HttpResponse
from perfil_apagno_app.models import Tarea
from categorias.models import Categoria

# Create your views here.

def initPerfil(request):
    return HttpResponse("Pagina de Perfil de usuario")

def tareas(request): #the index view
    mis_tareas = Tarea.objects.all()  # quering all todos with the object manager
    categorias = Categoria.objects.all()  # getting all categories with object manager

    if request.method == "GET":
        return render(request, "todoapp/index.html", {"tareas": mis_tareas, "categorias": categorias})