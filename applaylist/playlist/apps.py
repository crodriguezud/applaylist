from __future__ import unicode_literals

from django.apps import AppConfig
from django.contrib import algoliasearch

from .index import CancionIndex

class PlaylistConfig(AppConfig):
    name = 'playlist'

    def ready(self):
        Cancion = self.get_model('Cancion')
        algoliasearch.register(Cancion, CancionIndex)
