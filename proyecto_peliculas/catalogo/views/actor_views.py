from django.views.generic import DetailView
from catalogo.models import Actor

class ActorDetailView(DetailView):
    model = Actor
    template_name= "actor_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
