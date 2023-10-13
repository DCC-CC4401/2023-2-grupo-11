from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hola, este es un testeo")

def destacados_logged(request):
<<<<<<< HEAD
    return render(request, "destacados.html")
=======
    return render(request, "destacados.html")

def destacados(request):
    return render(request, "destacadosSL.html")
>>>>>>> 8433d6ba7485235a26698954b5f97b666e8cb32f
