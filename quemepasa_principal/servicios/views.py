from django.shortcuts import render
#importamos el modelo para poder acceder a los datos
from .models import Servicio

# Creamos las views para SERVICIOS

def servicios(request):
    #Accedemos a lo que hay en la base de datos.
    servicios = Servicio.objects.all()
    return render(request, 'servicios/servicios.html', {'servicios': servicios}) 
