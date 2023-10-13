from django.db import models

# Create your models here.
<<<<<<< HEAD

=======
'''
>>>>>>> 8433d6ba7485235a26698954b5f97b666e8cb32f
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    ubicacion = models.CharField(max_length=100)
<<<<<<< HEAD
    
=======
'''    
>>>>>>> 8433d6ba7485235a26698954b5f97b666e8cb32f
