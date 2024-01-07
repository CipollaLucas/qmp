from django.urls import path
from blog.views import *

# Creamos la variables para fusionar las views con las templates.

urlpatterns = [
    # path("", index, name="index"),
    path('', blog, name="blog"),
    path('categoria/<int:categoria_id>/', categoria, name="categoria"),
]
