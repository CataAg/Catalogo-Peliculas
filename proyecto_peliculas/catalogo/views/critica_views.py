from django.views.generic import DetailView
from catalogo.models import Pelicula
from django.db import models

class CriticaListView(DetailView):
    model = Pelicula
    template_name= "critica_list.html"

    def get_object(self):
        return super().get_object()

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       pelicula = self.get_object()
       #solo las criticas habilitadas
       criticas = pelicula.criticas.filter(habilitado=True).order_by("-pk")
       context["criticas"] = criticas
       return context
    
   

    



