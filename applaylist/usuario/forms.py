from django import forms
from django.forms import ModelForm
from .models import PlayList
from playlist.models import Cancion, Album, Artista
from django.contrib.auth.models import User

class CrearPlayListForm(ModelForm):

    def init_form_data(self, user):
        self.fields['creador'] = forms.ModelChoiceField(
            widget=forms.Select(
                attrs={
                    'class': 'datos_usuario form-control'
                }
            ),
            queryset=User.objects.filter(id=user.id),
            initial=User.objects.filter(id=user.id)[0]
        )

    class Meta:
        model = PlayList

        fields = ('nombre', 'creador',)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'datos_usuario form-control', 'placeholder': 'Nombre'}),
        }

    def clean(self):
        cleaned_data = super(CrearPlayListForm, self).clean()
        nombre = cleaned_data.get("nombre")
        creador = cleaned_data.get("creador")
        if PlayList.objects.filter(creador__id=creador.id, nombre=nombre).first() is not None:
            raise forms.ValidationError("Se ha creado la PlayList %s" % nombre)

class CrearCancionForm(ModelForm):

    class Meta:
        model = Cancion

        fields = ('nombre', 'album', 'artista', 'duracion', 'calificacion')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'datos_usuario form-control', 'placeholder': 'Nombre'}),
        }

    def clean(self):
        cleaned_data = super(CrearCancionForm, self).clean()
        nombre = cleaned_data.get("nombre")
        album = cleaned_data.get("album")
        if Cancion.objects.filter(album__id=album.id, nombre=nombre).first() is not None:
            raise forms.ValidationError("Se ha creado la Cancion %s" % nombre)

class CrearAlbumForm(ModelForm):

    class Meta:
        model = Album

        fields = ('nombre', 'artista')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'datos_usuario form-control', 'placeholder': 'Nombre'}),
        }

    def clean(self):
        cleaned_data = super(CrearAlbumForm, self).clean()
        nombre = cleaned_data.get("nombre")
        artista = cleaned_data.get("artista")
        if Album.objects.filter(artista__id=artista.id, nombre=nombre).first() is not None:
            raise forms.ValidationError("Se ha creado el Album %s" % nombre)

class CrearArtistaForm(ModelForm):

    class Meta:
        model = Artista

        fields = ('nombre',)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'datos_usuario form-control', 'placeholder': 'Nombre'}),
        }

    def clean(self):
        cleaned_data = super(CrearArtistaForm, self).clean()
        nombre = cleaned_data.get("nombre")
        if Artista.objects.filter(nombre=nombre).first() is not None:
            raise forms.ValidationError("Se ha creado el Artista %s" % nombre)


class AniadirCancionForm(ModelForm):
    class Meta:
        model = PlayList
        fields = ('caciones', 'nombre',)
