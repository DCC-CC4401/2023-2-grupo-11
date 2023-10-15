from django.http import HttpResponse
from django.shortcuts import render
from perfil_apagno_app.models import nuevoEvento
from django.core.paginator import Paginator

def destacados_logged(request):
    eventos = nuevoEvento.objects.all()  # Obtén todos los eventos desde la base de datos
    print("Eventos obtenidos:", eventos)  # Agrega esta línea para depuración
    paginator = Paginator(eventos, 6)
    page = request.GET.get('page')
    eventos = paginator.get_page(page)
    return render(request, "destacados.html", {'eventos': eventos})

#def destacados(request):
#    return render(request, "destacadosSL.html")

