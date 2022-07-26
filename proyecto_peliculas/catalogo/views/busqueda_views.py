from django.views.generic import TemplateView
from catalogo.models import Actor, Director
from itertools import chain

class BusquedaView(TemplateView):
    template_name = "search_result.html"

   