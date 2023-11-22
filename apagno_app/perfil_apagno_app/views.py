from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from perfil_apagno_app.forms import NuevoEventoForm
from perfil_apagno_app.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
# Imports for login and logout aunthentication
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.views import View
from .forms import UserUpdateForm, ProfileUpdateForm

# Create your views here.

def initPerfil(request):
    return HttpResponse("Pagina de Perfil de usuario")

def register_user(request):
    if request.method == 'GET': # When loading register page
        return render(request, "register_user.html") # Show template

    elif request.method == 'POST': # Getting form inputs
        # Take form elements coming as request.POST
        nombre = request.POST['nombre']
        contraseña = request.POST['contraseña']
        nombrereal = request.POST['nombrereal']
        apellidos = request.POST['apellidos']
        apodo = request.POST['apodo']
        pronombre = request.POST['pronombre']
        mail = request.POST['mail']

        # Creating new user
        user = User.objects.create_user(username=nombre, password=contraseña, first_name=nombrereal, last_name=apellidos, email=mail, nickname=apodo, pronouns=pronombre)

        #Redireccionar la página /tareas
        return HttpResponseRedirect('login') # '')

# request para la creacion del evento en la db
def login_user(request):
    # si el request es GET, se muestra el formulario
    if request.method == 'GET':
        return render(request,"login.html")
    # si el request es POST, se crea el evento
    if request.method == 'POST':
        username = request.POST['username']
        contraseña = request.POST['contraseña']
        usuario = authenticate(username=username,password=contraseña)
        if usuario is not None:
            login(request,usuario)
            return HttpResponseRedirect(reverse('eventos_destacados')) #'testeo2')
        else:
            return HttpResponseRedirect('register')
        
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('eventos_destacados'))#'crear_evento')

# request para la creacion del evento en el html
def creacionEvento(request):
    # obtencion de los datos en la db
    mis_eventos = nuevoEvento.objects.all()
    categorias = Categorias.objects.all()

    # si el request es GET, se muestra el formulario
    if request.method == "GET":
        return render(request, 'perfil_app/creacionEvento.html', {"eventos": mis_eventos, "categorias": categorias})
        #return render(request, 'destacados.html', {"eventos": mis_eventos, "categorias": categorias})
    
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
        

def creacionEvento2(request):
    # obtencion de los datos en la db
    mis_eventos = nuevoEvento.objects.all()
    categorias = Categorias.objects.all()
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
            return redirect('perfil_apagno_app')

    if request.method == "GET":
        return render(request, 'perfil_app/creacionEvento.html', {"eventos": mis_eventos, "categorias": categorias})
    
   

def evento_update(request, id):
    evento = nuevoEvento.objects.get(id=id)

    if request.method == 'POST':
        form = NuevoEventoForm(request.POST, instance=evento)
        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            return redirect('evento', evento.id)
    else:
        form = NuevoEventoForm(instance=evento)

    return render(request,'perfil_app/creacionEvento.html',{'form': form})


##----
class Eventos(ListView):
    model = nuevoEvento
    template_name = 'perfil_app/listaEventos.html'
    context_object_name = 'eventos'

    #def get_queryset(self):
    #    return nuevoEvento.objects.filter(host=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['eventos'] = context['eventos'].filter(host=self.request.user)
        context['categorias'] = Categorias.objects.all()
        return context
    
    def post(self,request):
        eventos = nuevoEvento.objects.all()
        categorias = Categorias.objects.all()

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
            return redirect('/perfil_apagno_app')
    

class EventoDetail(DetailView):
    model = nuevoEvento
    template_name = 'perfil_app/evento.html'
    context_object_name = 'evento'

    def get_queryset(self):
        base_qs = super(EventoDetail, self).get_queryset()
        return base_qs.filter(host=self.request.user)

class EventoUpdate(UpdateView):
    model = nuevoEvento
    template_name = 'perfil_app/editarEvento.html'
    fields = ['nombre', 'categoria', 'fecha', 'hora', 'lugar', 'descripcion', 'imagen']
    success_url = '/eventos_destacados'

    def form_valid(self, form):
        messages.success(self.request, 'Evento modificado exitosamente')
        return super(EventoUpdate, self).form_valid(form)
    
    def get_queryset(self):
        base_qs = super(EventoUpdate, self).get_queryset()
        return base_qs.filter(host=self.request.user)

class EventoDelete(LoginRequiredMixin, DeleteView):
    model = nuevoEvento
    template_name = 'perfil_app/elim_evento_confirm.html'
    context_object_name = 'evento'
    success_url = reverse_lazy('perfil')
    
    def form_valid(self, form):
        messages.success(self.request, "El evento se ha eliminado correctamente.")
        return super(EventoDelete,self).form_valid(form)
      
    def get_queryset(self):
        base_qs = super(EventoDelete, self).get_queryset()
        return base_qs.filter(host=self.request.user)


class MyProfile(LoginRequiredMixin, View):
    def get(self, request):
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        
        return render(request, 'perfil_app/profile.html', context)
    
    def post(self,request):
        user_form = UserUpdateForm(
            request.POST, 
            instance=request.user
        )
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            messages.success(request,'Your profile has been updated successfully')
            
            return redirect('perfil')
        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form
            }
            messages.error(request,'Error updating you profile')
            
            return render(request, 'perfil_app/profile.html', context)
            