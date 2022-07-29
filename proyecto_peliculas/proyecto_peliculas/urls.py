"""proyecto_peliculas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from catalogo.views import PeliculaView,PeliculaTemplateView,PeliculaListView
from catalogo.views import ActorDetailView,ActorListView, DirectorDetailView, DirectorListView
from catalogo.views import CriticaListView, CategoriaTemplateView, BusquedaView, CategoriaListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",PeliculaTemplateView.as_view(),name="home"),
    path("pelicula/<int:pk>/",PeliculaView.as_view(),name="pelicula-detail"),
    path("peliculas/",PeliculaListView.as_view(),name="pelicula-list"),
    path("pelicula/<int:pk>/criticas/",CriticaListView.as_view(),name="critica-list"),

    path("actor/<int:pk>/",ActorDetailView.as_view(),name="actor-detail"),
    path("actores/",ActorListView.as_view(),name="actor-list"),

    path("director/<int:pk>/",DirectorDetailView.as_view(),name="director-detail"),
    path("directores/",DirectorListView.as_view(),name="director-list"),

    path("categorias/",CategoriaTemplateView.as_view(),name="categorias"),
    path("categoria/<int:pk>/",CategoriaListView.as_view(),name="peliculas-categoria"),
    
    path("busqueda/",BusquedaView.as_view(),name="search-result"),

    #path("pelicula/<slug:titulo>/",PeliculaDetailView.as_view(),name="pelicula-detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

