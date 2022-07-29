from django.views.generic import ListView
from catalogo.models import Actor, Director, Pelicula, Categoria
from django.db.models import Q

class BusquedaView(ListView):
    template_name = "search_result.html"

    def get_queryset(self):
        query = self.request.GET.get('query')
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.get_queryset()
        context["query"] = query
        context["actores"]= Actor.objects.filter(Q(nombre__contains=query) | Q(apellido__contains=query))
        context["directores"] = Director.objects.filter(Q(nombre__contains=query) | Q(apellido__contains=query))
        context["peliculas"] = Pelicula.objects.filter(titulo__contains=query)
        context["categorias"] = Categoria.objects.filter(nombre__contains=query)
        return context
        



   