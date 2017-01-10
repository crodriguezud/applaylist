from __future__ import unicode_literals

from django.apps import AppConfig
from django.contrib import algoliasearch

from .index import CancionIndex, AlbumIndex, ArtistaIndex

class PlaylistConfig(AppConfig):
    name = 'playlist'

    def ready(self):
        Cancion = self.get_model('Cancion')
        algoliasearch.register(Cancion, CancionIndex)
        Album = self.get_model('Album')
        algoliasearch.register(Album, AlbumIndex)
        Artista = self.get_model('Artista')
        algoliasearch.register(Artista, ArtistaIndex)
        