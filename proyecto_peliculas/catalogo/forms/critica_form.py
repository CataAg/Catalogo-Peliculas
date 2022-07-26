from django.forms.models import inlineformset_factory
from django.forms import ModelForm
from django import forms
from catalogo.models import Critica
from django_starfield import Stars

class CriticaForm(ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Nombre"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Mail"}))
    comentario = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': '...'}))
    puntaje = forms.IntegerField(widget=Stars)
    
    class Meta:
        model = Critica
        exclude = ["habilitado"]
   

    

#criticasFormSet = inlineformset_factory(Pelicula,CriticaForm)