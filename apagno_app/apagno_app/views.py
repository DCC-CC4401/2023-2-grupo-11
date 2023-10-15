from django.http import HttpResponse
from django.shortcuts import render
from perfil_apagno_app.models import nuevoEvento

def destacados_logged(request):
    eventos = nuevoEvento.objects.all()  # Obtén todos los eventos desde la base de datos
    return render(request, "destacados.html", {'eventos':eventos})

#def destacados(request):
#    return render(request, "destacadosSL.html")

