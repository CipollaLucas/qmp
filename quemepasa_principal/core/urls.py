from django.contrib import admin
from django.urls import path
from core.views import *


urlpatterns = [
    # Acá traemos las urls de la app CORE.
    path('', HomePageView.as_view(), name='home'),
    path('historia/', HistoriaPageView.as_view(), name='historia'),
    path('terapias/', TerapiasPageView.as_view(), name='terapias'),
    #path('servicios/', servicios, name='servicios'),
    path('profesionales/', ProfesionalesPageView.as_view(), name='profesionales'),
    #path('contacto/', contacto, name='contacto'),
    #path('blog/', blog, name='blog'),
    #path('sample/', sample, name='sample'),
]
