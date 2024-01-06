from django.contrib import admin
from django.urls import path
from core.views import *


urlpatterns = [
    # Acá traemos las urls de la app CORE.
    path('', home, name='home'),
    path('historia/', historia, name='historia'),
    path('terapias/', terapias, name='terapias'),
    #path('servicios/', servicios, name='servicios'),
    path('store/', store, name='store'),
    path('contacto/', contacto, name='contacto'),
    path('blog/', blog, name='blog'),
    path('sample/', sample, name='sample'),
]
