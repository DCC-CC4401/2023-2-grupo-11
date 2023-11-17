from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from perfil_apagno_app.models import nuevoEvento
from datetime import datetime, time
from perfil_apagno_app.models import nuevoEvento


def destacados_logged(request):
    print("alo")
    # Obtener los parámetros de filtro de la solicitud GET
    categoria_filtro = request.GET.get('categoria', '')
    fecha_filtro = request.GET.get('fecha', '')
    hora_filtro = request.GET.get('hora', '')
    estado_filtro = request.GET.get('estado', '')

    ahora = datetime.now() # Se define la fecha y horas actuales

    # Obtener todos los eventos desde la base de datos
    eventos = nuevoEvento.objects.all()

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

    if request.method == "POST": 
        # Verificar si se ha enviado el formulario de "Apaño"
        print("holi")
        if 'apano_form' in request.POST:
            print("holi2")
            evento_id = request.POST.get("eventoId")
            evento = get_object_or_404(nuevoEvento, id=evento_id)
            print(evento_id)
            evento.asistentes.add(request.user)+
    


    
    return render(request, "destacados.html", {'eventos': eventos})


