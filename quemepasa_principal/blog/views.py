from django.shortcuts import render, get_object_or_404 #get_object_or_404 funciona como la consulta .all(), y se la pasan los parametros del Modelo, y el filtro.
from .models import Post, Categoria
# Create your views here.

def blog(request):
    posts= Post.objects.all()
    return render(request, 'blog/blog.html', {'posts' : posts})

def categoria (request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    return render(request, "blog/categoria.html", {'categoria': categoria})