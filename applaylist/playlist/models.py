from __future__ import unicode_literals
import time
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.encoding import smart_unicode

# Create your models here.

class Artista(models.Model):
	nombre = models.CharField(max_length=60)

	def get_albums(self):
		return Album.objects.filter(artista=self)

	def get_canciones(self):
		return merge(Cancion.objects.filter(album__artista=self),Cancion.objects.filter(artista=self))

	def __unicode__(self):
		return smart_unicode(self.nombre)

class Album(models.Model):
	nombre = models.CharField(max_length=60)
	artista = models.ForeignKey(Artista)

	def get_canciones(self):
		return Cancion.objects.filter(album=self)

	def get_numero_canciones(self):
		return len(Cancion.objects.filter(album=self))

	def __unicode__(self):
		return smart_unicode(self.nombre)

class Cancion(models.Model):
	nombre = models.CharField(max_length=60)
	duracion = models.IntegerField()
	album = models.ForeignKey(Album, blank=True, null=True)
	artista = models.ForeignKey(Artista, blank=True, null=True)
	calificacion = models.PositiveIntegerField(default=0)

	def get_duracion(self):
		return time.strftime("%M:%S", time.gmtime(self.duracion))

	def __unicode__(self):
		return smart_unicode(self.nombre)