from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from perfil_apagno_app.models import nuevoEvento, Categorias, User
from datetime import datetime, time
from perfil_apagno_app.models import nuevoEvento
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    categoria_filtro = request.GET.get('tipo', '')
    fecha_filtro = request.GET.get('fecha', '')
    hora_filtro = request.GET.get('hora', '')
    estado_filtro = request.GET.get('estado', '')

    ahora = datetime.now()  # Se define la fecha y horas actuales

    # Obtener todos los eventos desde la base de datos
    eventos_originales = nuevoEvento.objects.all()

    # Aplicar los filtros si se han especificado
    if categoria_filtro:
        eventos_originales = eventos_originales.filter(categoria__nombre=categoria_filtro)
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

    # Realizar la ordenación de eventos
    if request.method == "GET":
        # Obtener el valor del campo de orden
        orden = request.GET.get('orden')

        # Aplicar la ordenación
        if orden == 'fecha_asc':
            eventos_originales = eventos_originales.order_by('fecha')
        elif orden == 'fecha_desc':
            eventos_originales = eventos_originales.order_by('-fecha')
        else:
            eventos_originales = eventos_originales.order_by('-fecha')

    if request.method == "POST": 
        # Verificar si se ha enviado el formulario de "Apaño"
        print("Llega el POST")
        if "apano_form" in request.POST:
            print("Detecta formulario")
            evento_id = request.POST['eventoId']
            print("Detecta id del evento: ",evento_id)
            evento = get_object_or_404(nuevoEvento, id=evento_id)
            print(evento.asistentes.all())
            evento.asistentes.add(request.user)
            return HttpResponseRedirect(reverse('eventos_destacados'))

    # Realizar la paginación de eventos
    paginator = Paginator(eventos_originales, 4)  # 10 eventos por página
    page = request.GET.get('page', 1)

    try:
        eventos_paginados = paginator.page(page)
    except PageNotAnInteger:
        eventos_paginados = paginator.page(1)
    except EmptyPage:
        eventos_paginados = paginator.page(paginator.num_pages)

    return render(request, "destacados.html", {'eventos': eventos_paginados,'categorias': categorias})
