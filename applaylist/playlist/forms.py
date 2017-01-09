from django import forms
from django.forms import ModelForm
from .models import Cancion

class ActualizarCancionForm(ModelForm):

    class Meta:
        model = Cancion
        fields = ('calificacion','duracion',)

