from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import Thread, Message
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404, JsonResponse

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

#Peticion asincrona de los mensajes }
@login_required
def add_message(request, pk):
    print("Esto tiene request_GET:", request.GET)
    print("Esto tiene request.user: ", request.user)
    #vamos a retornar en un json
    json_response = {'created': False}
    #Recuperamos el contenido a partir del request
    if request.user:
        content = request.GET.get('content', None) #Recuperamos lo que haya, o none si esta vacío
        if content:
            thread = get_object_or_404(Thread, pk=pk) #recuperamos el hilo
            message = Message.objects.create(user=request.user, content=content)
            thread.messages.add(message) #Esto valdida con nuestra signal que el user existe.
            json_response['created'] = True #Si se ha creado el mensaje, se establece created a True.
    else:
        raise Http404("Usuario no identificado")
    return JsonResponse(json_response) #Aqui lo convierte en un diccionario pyton a Json. 

@login_required #Lo ahcemos porque necesitamos que el usuario este loggeado.
def start_thread(request, username):
    user = get_object_or_404(User, username=username) #recuperamos el usuario
    thread = Thread.objects.find_or_create(user, request.user) #recuperamos el hilo
    return redirect(reverse_lazy('messenger:detail', args=[thread.pk]))