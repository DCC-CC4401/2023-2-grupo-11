from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.
from django.utils import timezone
from PIL import Image

# User model:
# Has pronouns and nickname attributes.
class User(AbstractUser):
    pronounsChoices = [('La','La'),('El','El'), ('Le','Le'),('Otro','Otro')]
    pronouns = models.CharField(max_length=5,choices=pronounsChoices)
    nickname = models.CharField(max_length=30)
    contact = models.CharField(max_length=20, blank=True)
    
# Categorias crea una lista de categorias modificable desde el administrador de Django
# las categorias corresponden a los tipos de eventos posibles (a acordar)
class Categorias(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# nuevoEvento genera un evento nuevo con los siguientes atributos: nombre, host, fecha, hora, lugar, descripcion, categoria, imagen
# devuelve el evento en un formato apto para la base de datos
class nuevoEvento(models.Model):
    nombre = models.CharField(max_length=100)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    hora = models.TimeField(default=timezone.now().strftime("%H:%M"))
    lugar = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250, blank=True)
    categoria = models.ForeignKey(Categorias, default='Sin categoria', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='eventos_images/', blank=True)
    asistentes = models.ManyToManyField(User, related_name='eventos_asistir', blank=True)
    
    def __str__(self):
        return self.nombre

from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        default='default.jpg', # default avatar
        upload_to='profile_pics' # dir to store the image
    )
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        # save the profile first
        super().save(*args, **kwargs)

        # resize the image
        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            # create a thumbnail
            img.thumbnail(output_size)
            # overwrite the larger image
            img.save(self.avatar.path)
