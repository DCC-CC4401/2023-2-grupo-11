from django.shortcuts import render, redirect
from django.http import HttpResponse
from perfil_apagno_app.forms import NuevoEventoForm
from perfil_apagno_app.models import *
from django.http import HttpResponseRedirect
# Imports for login and logout aunthentication
from django.contrib.auth import authenticate, login, logout

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
            imagen = request.FILES.get('imagen', None)
            nuevo_evento = nuevoEvento(nombre=nombre, host=host, lugar=lugar, descripcion=descripcion, categoria=categoria, imagen=imagen)
            nuevo_evento.save()
            return redirect('/perfil_apagno_app/crear_evento')

def register_user(request):
    if request.method == 'GET': # When loading register page
     return render(request, "register_user.html") # Show template

    elif request.method == 'POST': # Getting form inputs
     # Take form elements coming as request.POST
     nombre = request.POST['nombre']
     contraseña = request.POST['contraseña']
     apodo = request.POST['apodo']
     pronombre = request.POST['pronombre']
     mail = request.POST['mail']

     # Creating new user
     user = User.objects.create_user(username=nombre, password=contraseña, email=mail, nickname=apodo, pronouns=pronombre)

     #Redireccionar la página /tareas
     return HttpResponseRedirect('')



def login_user(request):
    if request.method == 'GET':
        return render(request,"login.html")
    if request.method == 'POST':
        username = request.POST['username']
        contraseña = request.POST['contraseña']
        usuario = authenticate(username=username,password=contraseña)
        if usuario is not None:
            login(request,usuario)
            return HttpResponseRedirect('testeo2')
        else:
            return HttpResponseRedirect('register')
        
 
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('testeo2')
