from django.contrib import admin
# Personalizamos el admin de django. Importamos para activar.
from .models import Servicio

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Servicio, ServicioAdmin)

