from django.db import models

#modelo del formulario CONTACTO
class ContactoModelo(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre", null=False, blank=True )
    email = models.EmailField(max_length=50,verbose_name="Email", null=False, blank=True)
    contenido = models.CharField(max_length=300, verbose_name="Contenido", null=False, blank=True)
    created = models.DateTimeField(auto_now=True, verbose_name="Fecha de la consulta")

    class Meta:
        verbose_name= 'formulario_contacto'
        ordering = ['created']

    def __str__(self):
        return self.email
