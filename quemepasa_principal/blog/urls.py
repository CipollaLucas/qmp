from django.urls import path
from blog.views import index, About

# Creamos la variables para mezclar las views con las templates.

urlpatterns = [
    # path("", index, name="index"),
    path("about", About, name="about"),
]
