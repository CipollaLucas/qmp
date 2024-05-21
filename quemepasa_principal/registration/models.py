from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#Vamos a crear el profile

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Esta realacion 1:1, hace que sólo exista un perfil por un usuario.
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
