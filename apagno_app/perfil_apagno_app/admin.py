from django.contrib import admin
#from perfil_apagno_app
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(nuevoEvento)
admin.site.register(Categorias)
admin.site.register(Profile)