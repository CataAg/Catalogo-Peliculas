from django.views.generic import DetailView, TemplateView, ListView
from django.views import View
from catalogo.forms import CriticaForm
from django.views.generic.edit import FormView, SingleObjectMixin
from catalogo.models import Pelicula
from django.urls import reverse

class PeliculaDetailView(DetailView):
    model = Pelicula
    template_name= "pelicula_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pelicula = self.get_object()
        puntaje = self.get_object().puntaje 
        # Las 3 criticas mas recientes
        criticas = pelicula.criticas.filter(habilitado=True).order_by('-pk')[:3] 
        #El puntaje se envia por context para poder vincularlo con las estrellas en el template
        context["puntaje"] = puntaje
        context["criticas_recientes"] = criticas
        #Asigno la pelicula actual, que recibi por get_object(), como la pelicula para el form de critica
        context["form"] = CriticaForm(initial={"pelicula":pelicula})
        categorias = pelicula.categorias
        context["categorias"] = categorias
        return context

#Para poder tener la seccion "agregar critica" dentro del detalle de pelicula
class PeliculaCriticaView(SingleObjectMixin,FormView):
    template_name = "pelicula_detail.html"
    form_class = CriticaForm
    model = Pelicula
 
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse('pelicula-detail', kwargs={'pk' : self.object.pk})

class PeliculaView(View):
    def get(self, request, *args, **kwargs):
        view = PeliculaDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PeliculaCriticaView.as_view()
        return view(request, *args, **kwargs)

#vista grilla principal
class PeliculaTemplateView(TemplateView):
    template_name= "grilla.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #"-puntaje" para que el orden sea de mayor a menor
        peliculas = Pelicula.objects.all().order_by("-puntaje")[:12]
        context["peliculas"] = peliculas
        return context
        
#vista seccion peliculas
class PeliculaListView(ListView):
    model = Pelicula
    paginate_by = 10
    template_name="pelicula_list.html"
    ordering = ["titulo"]
