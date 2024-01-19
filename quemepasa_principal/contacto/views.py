from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm

# Create your views here.
def contacto(request):
    print(request.POST)
    form_contacto = ContactForm()
    #Si detecta que hay un post, lo procesamos
    if request.POST:
        form_contacto = ContactForm(data=request.POST) #* Rellenamos el formulario con el diccionario que traemos con la data.
        if form_contacto.is_valid():
            nombre = request.POST.get('nombre','')
            email = request.POST.get('email','')
            contenido = request.POST.get('contenido','')
            #Si todo va bien, redireccionamos
            return redirect(reverse('contacto')+"?ok")

    return render(request, 'contacto/contacto.html', {'form_contacto': form_contacto})