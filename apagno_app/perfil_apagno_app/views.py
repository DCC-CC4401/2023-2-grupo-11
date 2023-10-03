from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def initPerfil(request):
    return HttpResponse("Pagina de Perfil de usuario")