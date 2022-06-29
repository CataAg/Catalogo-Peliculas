from django.contrib import admin
from catalogo.models import Actor, Director, Pelicula, Categoria, Critica

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display=["nombre","apellido","fecha_nacimiento","nacionalidad"]
#admin.site.register(Actor,ActorAdmin)

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display=["nombre","apellido","fecha_nacimiento","nacionalidad"]

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display=["titulo","director","puntaje","fecha_lanzamiento"]

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display=["nombre"]
    
@admin.action(description="Habilitar comentario")
def habilitar_comentario(modeladmin,request,queryset):
    queryset.update(habilitado=True)

@admin.register(Critica)
class CriticaAdmin(admin.ModelAdmin):
    list_display= ["comentario","habilitado","puntaje","pelicula"]
    actions=[habilitar_comentario]

    #quito el permiso de crear criticas desde la pagina admin
    def has_add_permission(self, request, obj=None):
        return False
    
    