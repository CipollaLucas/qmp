#Creamos este fichero con esta función para poder enviar contextos a cualquier template.
# * IMPORTANTE: registar en settings.py principal dicho fichero y función, en el apartado de TEMPLATES/CONTEXT_PROCESSORS.
from .models import Link


def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx