from django.contrib import admin
#from perfil_apagno_app
from .models import nuevoEvento, Categorias

# Register your models here.
admin.site.register(nuevoEvento)
admin.site.register(Categorias)