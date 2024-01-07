from django.db import models
from django.utils.timezone import now #utilizamos de esta manera porque, si llama al método now(), va a analizar la hora del servidor en cada llamada.
from django.contrib.auth.models import User #Importamos el modelo de usuario.

# Definimos lo modelos que vamos a utilizar en el Blog

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['-created']

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Titulo")
    contenido = models.TextField(verbose_name="Contenido")
    publicado = models.DateTimeField(verbose_name="Fecha de publicación", default=now) #Podrá elegir fecha de publicacion, sino, se le asignará el actual por defecto.
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True) # La imagen no será obligatoria.
    #Autor va a ser enlazada con una foreignkey del admin de usuarios que trae Django por defecto.
    autor = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria, verbose_name="Categorías", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "posteo"
        verbose_name_plural = "posteos"
        ordering = ['-created']

    def __str__(self):
        return self.titulo