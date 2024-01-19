#Creamos este fichero con esta función para poder enviar contextos a cualquier template.
# * IMPORTANTE: registar en settings.py principal dicho fichero y función, en el apartado de TEMPLATES/CONTEXT_PROCESSORS.
from .models import Page


def ctx_dict(request):
    ctx = {}
    paginas = Page.objects.all()
    for pagina in paginas:
        ctx[pagina.key] = pagina.content
    return ctx