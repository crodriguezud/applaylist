from django.contrib.algoliasearch import AlgoliaIndex


class CancionIndex(AlgoliaIndex):
    fields = ('nombre', 'nombre_slug', 'album', 'artista', 'calificacion')
    settings = {'attributesToIndex': ['nombre']}
    index_name = 'nombre_cancion_index'
