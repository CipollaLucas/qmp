from django.db import models

#Definimos la clase Servicios
class Servicio(models.Model):
    
    titulo = models.CharField(max_length=200, verbose_name="Título")
    subtitulo = models.CharField(max_length=200, verbose_name="sub título") 
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Image", upload_to="servicios")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ['-created']

    def __str__(self):
        return self.titulo