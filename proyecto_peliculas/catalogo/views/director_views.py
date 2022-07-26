from django.views.generic import DetailView
from catalogo.models import Director

class DirectorDetailView(DetailView):
    model = Director
    template_name= "director_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
