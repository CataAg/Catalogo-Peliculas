from django.views.generic import DetailView, ListView
from catalogo.models import Director

class DirectorDetailView(DetailView):
    model = Director
    template_name= "persona_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #para seccion filmografia destacada
        peliculas = self.get_object().peliculas.order_by("-puntaje")[:4]
        context["peliculas"] = peliculas
        return context

class DirectorListView(ListView):
    model = Director
    paginate_by=10
    template_name= "director_list.html"
    ordering= ["apellido", "nombre"]
