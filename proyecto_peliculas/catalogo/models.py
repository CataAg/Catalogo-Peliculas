from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator,MaxValueValidator

class Actor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="media/actores")
    fecha_nacimiento = models.DateField()
    nacionalidad = CountryField() #libreria para facilitar la carga de los paises
    biografia = models.CharField(max_length=300,null=True,blank = True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido
 
class Director(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="media/directores")
    fecha_nacimiento = models.DateField()
    nacionalidad = CountryField()
    biografia = models.CharField(max_length=300,null=True,blank=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre 

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    resumen= models.CharField(max_length=300)
    imagen = models.ImageField(upload_to="media/peliculas",null = True)
    actores = models.ManyToManyField(Actor)
    director = models.ForeignKey(Director,on_delete=models.CASCADE)
    fecha_lanzamiento = models.DateField()
    categorias = models.ManyToManyField(Categoria)
    puntaje = models.IntegerField(default=1)

    def get_puntaje(self):
        total_puntajes = 0
        sumatoria_puntajes = 0

        for critica in self.criticas.all():
            total_puntajes += 1
            sumatoria_puntajes += critica.puntaje
        
        self.puntaje = (sumatoria_puntajes/total_puntajes)
        self.save()
    
        return round(sumatoria_puntajes / total_puntajes)
    
    def __str__(self):
        return self.titulo + " (" + str(self.fecha_lanzamiento.year) + ")"

    #Mostrar solo las criticas habilitadas en la seccion de criticas del detalle de Pelicula
    def criticas_habilitadas(self):
        return self.criticas.filter(habilitado=True)

class Critica(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    comentario = models.CharField(max_length=300)
    puntaje = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    habilitado = models.BooleanField(default=False)
    pelicula = models.ForeignKey(Pelicula,on_delete=models.CASCADE,null=True,related_name="criticas")

    def __str__(self):
        return self.nombre + " " + self.pelicula.titulo + "puntaje: " + str(self.puntaje)
    
    def habilitar(self):
        self.habilitado = True
        self.save()

    def save(self,*args, **kwargs):
        if self.pelicula.criticas.count() > 1:
            self.pelicula.puntaje = self.pelicula.get_puntaje()
        super(Critica,self).save(*args,**kwargs)







