from django.shortcuts import render

# Create your views here.


def index(request):

    # Render recibe tres parametros (peticion request, template y contexto a renderizar.)
    return render(request, 'index.html')


def About(request):
    return render(request, 'blog/about.html')
