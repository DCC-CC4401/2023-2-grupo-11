from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from perfil_apagno_app.models import nuevoEvento
from datetime import datetime, time
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def destacados_logged(request):
    # Obtener los parámetros de filtro de la solicitud GET
    categoria_filtro = request.GET.get('categoria', '')
    fecha_filtro = request.GET.get('fecha', '')
    hora_filtro = request.GET.get('hora', '')
    estado_filtro = request.GET.get('estado', '')

    ahora = datetime.now() # Se define la fecha y horas actuales

    # Obtener todos los eventos desde la base de datos
    eventos_originales = nuevoEvento.objects.all()

    # Aplicar los filtros si se han especificado
    if categoria_filtro:
        eventos_originales = eventos_originales.filter(tipo=categoria_filtro)
    if fecha_filtro:
        eventos_originales = eventos_originales.filter(fecha=fecha_filtro)
    if hora_filtro:
        if hora_filtro == "6-14":
            eventos_originales = eventos_originales.filter(hora__gte=time(6, 0), hora__lt=time(14, 0))
        elif hora_filtro == "14-20":
            eventos_originales = eventos_originales.filter(hora__gte=time(14, 0), hora__lt=time(20, 0))
        elif hora_filtro == "20-6":
            eventos_originales = eventos_originales.filter(hora__gte=time(20, 0)) | eventos_originales.filter(hora__lt=time(6, 0))

    if estado_filtro == "terminado":
        eventos_originales = eventos_originales.filter(fecha__lt=ahora.date())
        eventos_originales = eventos_originales.exclude(fecha=ahora.date(), hora__gt=ahora.time())
    elif estado_filtro == "sin_comenzar":
        eventos_originales = eventos_originales.filter(fecha__gt=ahora.date())
        eventos_originales = eventos_originales.exclude(fecha=ahora.date(), hora__lte=ahora.time())

    # Realizar la paginación de eventos
    paginator = Paginator(eventos_originales, 4)  # 10 eventos por página
    page = request.GET.get('page', 1)

    try:
        eventos = paginator.page(page)
    except PageNotAnInteger:
        eventos = paginator.page(1)
    except EmptyPage:
        eventos = paginator.page(paginator.num_pages)

    if request.method == "GET":
        # Obtener el valor del campo de orden
        orden = request.GET.get('orden')

        # Realiza el procesamiento necesario para ordenar los eventos según la opción seleccionada
        # Aplicar la ordenación
        if orden == 'fecha_asc':
            eventos_originales = eventos_originales.order_by('fecha')
        elif orden == 'fecha_desc':
            eventos_originales = eventos_originales.order_by('-fecha')
        else:
            eventos_originales = eventos_originales.order_by('-fecha')

    return render(request, "destacados.html", {'eventos': eventos})


