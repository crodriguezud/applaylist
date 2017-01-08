from django.contrib.auth.decorators import login_required

from django.conf.urls import url

# Import Class Based Views
from .views import UsuarioView, CrearPlayListView, PlayListView, CrearCancionView, AniadirCancionView
from playlist.views import CancionesView

urlpatterns = [
    url(r'^$', login_required(UsuarioView.as_view()), name='user_profile'),
    url(r'^crear-playlist/$', login_required(CrearPlayListView.as_view()), name='user_create_playlist'),
    url(r'^playlist/(?P<playlist_slug>[\w-]+)/$', login_required(PlayListView.as_view()), name='user_playlists'),
    url(r'^crear-cancion/$', login_required(CrearCancionView.as_view()), name='user_create_cancion'),
    url(r'^playlist/(?P<playlist_slug>[\w-]+)/aniadir-cancion/$', login_required(CancionesView.as_view()), name='user_add_cancion'),
    url(r'^playlist/(?P<playlist_slug>[\w-]+)/aniadir-cancion/(?P<cancion_slug>[\w-]+)/$', login_required(AniadirCancionView.as_view()), name='user_add_cancion'),
    ]
