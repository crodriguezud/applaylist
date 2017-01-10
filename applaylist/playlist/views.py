from django.shortcuts import render

from django.views.generic import DetailView, ListView, UpdateView
from .models import Cancion, Album, Artista
from usuario.models import PlayList
from .forms import ActualizarCancionForm
from django.shortcuts import redirect
from applaylist.utils import cliente_pusher

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

class CancionesListView(ListView):
    model = Cancion
    template_name = 'lista_listacanciones.html'  

    def get_context_data(self, **kwargs):
        context = super(CancionesListView, self).get_context_data(**kwargs)
        return context

class AlbumListView(ListView):
    model = Album
    template_name = 'lista_abum.html'  

    def get_context_data(self, **kwargs):
        context = super(AlbumListView, self).get_context_data(**kwargs)
        return context

class ArtistasListView(ListView):
    model = Artista
    template_name = 'lista_artista.html'  

    def get_context_data(self, **kwargs):
        context = super(ArtistasListView, self).get_context_data(**kwargs)
        return context

class CancionesView(ListView):
    model = Cancion
    template_name = 'lista_canciones.html'  

    def get_context_data(self, **kwargs):
		context = super(CancionesView, self).get_context_data(**kwargs)
		if self.kwargs['playlist_slug']:
			playlist = PlayList.objects.get(nombre_slug=self.kwargs['playlist_slug'])
			lista_canciones = []
			for cancion in list(playlist.caciones.all()):
				lista_canciones.append(cancion.id)
			context['canciones'] = Cancion.objects.all().exclude(id__in=lista_canciones)
		else:
			context['canciones'] = Cancion.objects.all()
		return context

class CalificarCancionView(UpdateView):

    def get(self, request, *args, **kwargs):
        cancion = Cancion.objects.get(nombre_slug=self.kwargs['cancion_slug'])
        cancion.calificacion = (cancion.calificacion + int(self.kwargs['calificacion']))/2
        cancion.save()
        cliente_pusher.trigger('ApPlayList', 'calificar', {'cancion': cancion.nombre})
        return redirect('/playlist/cancion/'+self.kwargs['cancion_slug'])