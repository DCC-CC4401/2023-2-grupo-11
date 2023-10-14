from django.db import models

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    ubicacion = models.CharField(max_length=100)