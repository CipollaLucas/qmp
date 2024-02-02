from django.shortcuts import render
from django.views.generic.base import TemplateView
#Acá vamos a tener las views estáticas

#Vamos a utilizar vistas basadas en clases.
class HomePageView(TemplateView):
    template_name = 'core/home.html'
    def get(self, request, *args, **kargs):
        return render(request, self.template_name)

class HistoriaPageView(TemplateView):
    template_name = 'core/historia.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name )

class ProfesionalesPageView(TemplateView):
    template_name = 'core/profesionales.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name )

class TerapiasPageView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name )
