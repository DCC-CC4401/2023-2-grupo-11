from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# importing custom User class
from perfil_apagno_app.models import User       

# Create your views here.

def initPerfil(request):
    return HttpResponse("Pagina de Perfil de usuario")

def register_user(request):
    if request.method == 'GET': # When loading register page
     return render(request, "perfil_apagno_app/register_user.html") # Show template

    elif request.method == 'POST': # Getting form inputs
     # Take form elements coming as request.POST
     nombre = request.POST['nombre']
     contraseña = request.POST['contraseña']
     apodo = request.POST['apodo']
     pronombre = request.POST['pronombre']
     mail = request.POST['mail']

     # Creating new user
     user = User.objects.create_user(username=nombre, password=contraseña, email=mail, nickname=apodo, pronoun=pronombre)

     #Redireccionar la página /tareas
     return HttpResponseRedirect('')