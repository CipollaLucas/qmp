from django.shortcuts import render

#Acá vamos a tener las views estáticas


def home(request):

    # Render recibe tres parametros (peticion request, template y contexto a renderizar.)
    return render(request, 'core/home.html')

def historia(request):
    return render(request, 'core/historia.html')

def store(request):
    return render(request, 'core/store.html')

def terapias(request):
    return render (request, "core/terapias.html")
