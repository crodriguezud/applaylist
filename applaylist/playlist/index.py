from django.contrib.algoliasearch import AlgoliaIndex


class CancionIndex(AlgoliaIndex):
    fields = ('nombre', 'nombre_slug', 'album', 'artista', 'calificacion')
    settings = {'attributesToIndex': ['nombre']}
    index_name = 'nombre_cancion_index'

class AlbumIndex(AlgoliaIndex):
    fields = ('nombre', 'nombre_slug', 'artista')
    settings = {'attributesToIndex': ['nombre']}
    index_name = 'nombre_album_index'

class ArtistaIndex(AlgoliaIndex):
    fields = ('nombre', 'nombre_slug')
    settings = {'attributesToIndex': ['nombre']}
    index_name = 'nombre_artista_index'
