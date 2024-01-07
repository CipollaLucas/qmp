from django.contrib import admin
from django.urls import path
from servicios.views import *


urlpatterns = [
    # Acá traemos las urls de la app SERVICIOS.
    path('', servicios, name='servicios'),

]
