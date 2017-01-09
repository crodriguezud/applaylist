from django.contrib.auth.decorators import login_required

from django.conf.urls import url

# Import Class Based Views
from .views import CancionView, AlbumView, ArtistaView, CancionesListView, AlbumListView, CalificarCancionView, ArtistasListView

urlpatterns = [
    url(r'^cancion/(?P<cancion_slug>[\w-]+)/$', CancionView.as_view(), name='user_cancion'),
    url(r'^canciones/(?P<cancion_slug>[\w-]+)/$', CancionView.as_view(), name='user_cancion'),
    url(r'^album/(?P<album_slug>[\w-]+)/$', AlbumView.as_view(), name='user_album'),
    url(r'^artista/(?P<artista_slug>[\w-]+)/$', ArtistaView.as_view(), name='user_artista'),
    url(r'^canciones/$', CancionesListView.as_view(), name='user_canciones'),
    url(r'^albumes/$', AlbumListView.as_view(), name='user_albumes'),
    url(r'^artistas/$', ArtistasListView.as_view(), name='user_artistas'),
    url(r'^cancion/(?P<cancion_slug>[\w-]+)/calificar/$', CalificarCancionView.as_view(), name='user_calificar_cancion'),
    ]
