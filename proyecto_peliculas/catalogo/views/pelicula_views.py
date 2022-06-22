from django.views.generic import DetailView, TemplateView
from catalogo.models import Pelicula

class PeliculaDetailView(DetailView):
    model = Pelicula
    template_name= "pelicula_detail.html"

    def get_object(self):
        return super().get_object()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        puntaje = self.get_object().puntaje
        context["puntaje"] = puntaje
        return context

class PeliculaTemplateView(TemplateView):
    template_name= "grilla.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        peliculas = Pelicula.objects.all()
        context["peliculas"] = peliculas
        return context
