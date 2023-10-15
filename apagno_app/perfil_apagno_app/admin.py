from django.contrib import admin
#from perfil_apagno_app
from .models import nuevoEvento, Categorias, User

admin.site.register(User)
# Register your models here.
admin.site.register(nuevoEvento)
admin.site.register(Categorias)