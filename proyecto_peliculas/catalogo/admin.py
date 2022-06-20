from django.contrib import admin
from catalogo.models import Actor, Director, Pelicula, Categoria, Critica

# Register your models here.
class ActorAdmin(admin.ModelAdmin):
    #actions = [cambiar_nombre]
    pass
admin.site.register(Actor,ActorAdmin)

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    pass

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    pass

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Critica)
class CriticaAdmin(admin.ModelAdmin):
    pass

#admin actions
@admin.action(description="pasar a uppercase")
def cambiar_nombre(modeadmin,request,queryset):
    pass
    #for actor in queryset:
    #    actor.nombre = actor.nombre.upper()
    #    actor.save()

#las actions se indican por medio de una lista
#actions =[action_nombre]
