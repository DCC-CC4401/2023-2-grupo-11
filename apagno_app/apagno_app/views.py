from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from perfil_apagno_app.models import nuevoEvento, Categorias, User
from datetime import datetime, time


def destacados_logged(request):
    # Obtener todos los eventos desde la base de datos
    eventos = nuevoEvento.objects.all()
    categorias = Categorias.objects.all()
    # si el request es POST, se crea el evento
    if request.method == "POST":
        if "eventAdd" in request.POST:
            nombre = request.POST['nombre']
            host = User.objects.get(username=request.user.username)
            fecha = request.POST['fecha']
            hora = request.POST['hora']
            lugar = request.POST['lugar']
            descripcion = request.POST['descripcion']
            categoria = Categorias.objects.get(nombre=request.POST["selector_categoria"])
            imagen = request.FILES.get('imagen', None)
            nuevo_evento = nuevoEvento(nombre=nombre, host=host, fecha=fecha, hora=hora, lugar=lugar, descripcion=descripcion, categoria=categoria, imagen=imagen)
            nuevo_evento.save()
            return redirect('/eventos_destacados')
    # Obtener los parámetros de filtro de la solicitud GET
    categoria_filtro = request.GET.get('categoria', '')
    fecha_filtro = request.GET.get('fecha', '')
    hora_filtro = request.GET.get('hora', '')
    estado_filtro = request.GET.get('estado', '')

    ahora = datetime.now() # Se define la fecha y horas actuales

   

    # Aplicar los filtros si se han especificado
    if categoria_filtro:
        eventos = eventos.filter(tipo=categoria_filtro)
    if fecha_filtro:
        eventos = eventos.filter(fecha=fecha_filtro)
    if hora_filtro:
        if hora_filtro == "6-14":
            eventos = eventos.filter(hora__gte=time(6, 0), hora__lt=time(14, 0))
        elif hora_filtro == "14-20":
            eventos = eventos.filter(hora__gte=time(14, 0), hora__lt=time(20, 0))
        elif hora_filtro == "20-6":
            eventos = eventos.filter(hora__gte=time(20, 0)) | eventos.filter(hora__lt=time(6, 0))

    if estado_filtro == "terminado":
        eventos = eventos.filter(fecha__lt=ahora.date())
        eventos = eventos.exclude(fecha=ahora.date(), hora__gt=ahora.time())
    elif estado_filtro == "sin_comenzar":
        eventos = eventos.filter(fecha__gt=ahora.date())
        eventos = eventos.exclude(fecha=ahora.date(), hora__lte=ahora.time())
    
    if request.method == "GET":
        # Obtener el valor del campo de orden
        orden = request.GET.get('orden')

        # Realiza el procesamiento necesario para ordenar los eventos según la opción seleccionada
        # Aplicar la ordenación
        if orden == 'fecha_asc':
            eventos = eventos.order_by('fecha')
        elif orden == 'fecha_desc':
            eventos = eventos.order_by('-fecha')
        else:
            eventos = eventos.order_by('-fecha')
    
    return render(request, "destacados.html", {'eventos': eventos,'categorias': categorias})


