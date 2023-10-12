from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.


# User model:
# Has pronouns and nickname attributes.
class User(AbstractUser):
  pronounsChoices = [('La','La'),('El','El'), ('Le','Le'),('Otro','Otro')]
  pronouns = models.CharField(max_length=5,choices=pronounsChoices)
  nickname = models.CharField(max_length=30)
  contact = models.CharField(max_length=100, blank=True)


