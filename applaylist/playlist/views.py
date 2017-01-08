from django.shortcuts import render

from django.views.generic import DetailView, ListView
from .models import Cancion, Album, Artista
from usuario.models import PlayList

# Create your views here.
class CancionView(DetailView):
    model = Cancion
    template_name = 'cancion.html'
    slug_url_kwarg = 'cancion_slug'
    slug_field = 'nombre_slug'

class AlbumView(DetailView):
    model = Album
    template_name = 'album.html'
    slug_url_kwarg = 'album_slug'
    slug_field = 'nombre_slug'

class ArtistaView(DetailView):
    model = Artista
    template_name = 'artista.html'
    slug_url_kwarg = 'artista_slug'
    slug_field = 'nombre_slug'

class CancionesView(ListView):
    model = Cancion
    template_name = 'lista_canciones.html'  

    def get_context_data(self, **kwargs):
        context = super(CancionesView, self).get_context_data(**kwargs)
        playlist = PlayList.objects.get(nombre_slug=self.kwargs['playlist_slug'])
        lista_canciones = []
        for cancion in list(playlist.caciones.all()):
        	lista_canciones.append(cancion.id)
        context['canciones'] = Cancion.objects.all().exclude(id__in=lista_canciones)
        return context