from django import forms
from .models import *

class NewsFormulario(forms.Form):
    titulo = models.CharField(max_length=50)
    subtitulo= models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=150)
    autor = models.CharField(max_length=50)
    fecha = models.DateTimeField(max_length=50)