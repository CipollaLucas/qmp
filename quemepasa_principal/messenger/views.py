from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import Thread
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404

# Creamos las vistas.

#Esto devuelve todas las instancias que existen, pero vamos a filtrarlas.
@method_decorator(login_required, name='dispatch') # Usamos este decorador para poder comprobar que el usuario inicio sesión.
class ThreadList(TemplateView):
    template_name = "messenger/thread_list.html"

@method_decorator(login_required, name='dispatch') # Usamos este decorador para poder comprobar que el usuario inicio sesión.
class ThreadDetail(DetailView):
    model = Thread

    #sobreescribimos el get_object. Solo maneja una instancia
    def get_object(self):
        obj = super(ThreadDetail, self).get_object() #Simula recuperar el objecto
        if self.request.user not in obj.users.all(): #Comprobamos si el usuario identificado no se encuentra
            raise Http404()
        return obj