from django import template
from pages.models import Page

# Ahora la registramos en la librería de templates.
register = template.Library()

# Con este decorador transformamos la funcion en un simple tag.
@register.simple_tag
def get_page_list():             # Con esta función recuperamos todas las paginas.
    pages = Page.objects.all()
    return pages #Esto es lo que devolvemos en forma de TEMPLATE_TAG