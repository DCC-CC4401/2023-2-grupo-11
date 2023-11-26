from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Profile model:
# Tiene un campo de usuario y un campo de avatar.
# create_profile crea el perfil.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Profile model:
# Tiene un campo de usuario y un campo de avatar.
# save_profile guarda el perfil.
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()