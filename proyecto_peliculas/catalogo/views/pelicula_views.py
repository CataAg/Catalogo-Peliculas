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
        #categorias = self.get_object().categorias
        #context["categorias"] = categorias
        #El puntaje se envia por context para poder vincularlo con las estrellas en el template
        return context

class PeliculaTemplateView(TemplateView):
    template_name= "grilla.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #"-puntaje" para que el orden sea de mayor a menor
        peliculas = Pelicula.objects.all().order_by("-puntaje")[:12]
        context["peliculas"] = peliculas
        return context
