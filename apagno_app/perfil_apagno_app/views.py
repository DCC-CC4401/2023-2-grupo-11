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

# request para la creacion del evento en la db
def login_user(request):
    # si el request es GET, se muestra el formulario
    if request.method == 'GET':
        return render(request,"login.html")
    # si el request es POST, se crea el evento
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

# request para la creacion del evento en el html
def creacionEvento(request):
    # obtencion de los datos en la db
    mis_eventos = nuevoEvento.objects.all()
    categorias = Categorias.objects.all()

    # si el request es GET, se muestra el formulario
    if request.method == "GET":
        return render(request, 'perfil_app/creacionEvento.html', {"eventos": mis_eventos, "categorias": categorias})
    
    # si el request es POST, se crea el evento
    if request.method == "POST":
        if "eventAdd" in request.POST:
            nombre = request.POST['nombre']
            host = User.objects.get(username=request.user.username)
            lugar = request.POST['lugar']
            descripcion = request.POST['descripcion']
            categoria = Categorias.objects.get(nombre=request.POST["selector_categoria"])
            imagen = request.FILES.get('imagen', None)
            nuevo_evento = nuevoEvento(nombre=nombre, host=host, lugar=lugar, descripcion=descripcion, categoria=categoria, imagen=imagen)
            nuevo_evento.save()
            return redirect('/eventos_destacados')
