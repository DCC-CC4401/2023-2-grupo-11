from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hola, este es un testeo")

def destacados_logged(request):
    return render(request, "base.html")