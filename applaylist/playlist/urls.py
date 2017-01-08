from django.contrib.auth.decorators import login_required

from django.conf.urls import url

# Import Class Based Views
from .views import CancionView, AlbumView, ArtistaView, CancionesView

urlpatterns = [
    url(r'^cancion/(?P<cancion_slug>[\w-]+)/$', login_required(CancionView.as_view()), name='user_cancion'),
    url(r'^album/(?P<album_slug>[\w-]+)/$', login_required(AlbumView.as_view()), name='user_album'),
    url(r'^artista/(?P<artista_slug>[\w-]+)/$', login_required(ArtistaView.as_view()), name='user_artista'),
    url(r'^canciones/$', login_required(CancionesView.as_view()), name='user_canciones'),
    ]
