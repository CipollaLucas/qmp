from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

#Método para optimizar las imagenes
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

#Vamos a crear el profile

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Esta realacion 1:1, hace que sólo exista un perfil por un usuario.
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['user__last_name']

#Vamos a decorar la funcion para poder enviar la señal
@receiver(post_save, sender=User) # Usamos post_save para que la señal se envíe luego del registro.
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print("Se crea un usuario, y el perfil.")