from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.utils import timezone

class Categorias(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
cats = Categorias.objects.all().values_list('nombre', 'nombre')
cats_list = []
for item in cats:
    cats_list.append(item)

# nuevoEvento genera un evento nuevo con los siguientes atributos: nombre, host, fecha, hora, lugar, descripcion, categoria, imagen
class nuevoEvento(models.Model):
    nombre = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    fecha = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    hora = models.TimeField(default=timezone.now().strftime("%H:%M"))
    lugar = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250, blank=True)
    categoria = models.ForeignKey(Categorias, default='Sin categoria', on_delete=models.CASCADE)#models.CharField(max_length=100, default='Sin categoria')
    imagen = models.ImageField(upload_to='eventos_images/', blank=True)
    
    def __str__(self):
        return self.nombre
    
# User model:
# Has pronouns and nickname attributes.
class User(AbstractUser):
  pronounsChoices = [('La','La'),('El','El'), ('Le','Le'),('Otro','Otro')]
  pronouns = models.CharField(max_length=5,choices=pronounsChoices)
  nickname = models.CharField(max_length=30)
  contact = models.CharField(max_length=100, blank=True)
