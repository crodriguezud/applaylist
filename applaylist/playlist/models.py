from __future__ import unicode_literals
import time
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.encoding import smart_unicode
from django.db.models import Q

# Create your models here.

def cargar_imagen(instance, filename):
    return 'artits/%s/%s' % (instance.username, filename)

class Artista(models.Model):
	nombre = models.CharField(max_length=50)
	nombre_slug = models.SlugField(max_length=50, blank=True, null=True)

	def save(self, *args, **kwargs):
		self.nombre_slug = slugify(self.nombre)
		super(self.__class__, self).save(*args, **kwargs)

	def get_albums(self):
		return Album.objects.filter(artista=self)

	def get_canciones(self):
		return Cancion.objects.filter(Q(album__artista=self) | Q(artista=self))

	def __unicode__(self):
		return smart_unicode(self.nombre)

class Album(models.Model):
	nombre = models.CharField(max_length=60)
	nombre_slug = models.SlugField(max_length=50, blank=True, null=True)
	artista = models.ForeignKey(Artista)
	
	def save(self, *args, **kwargs):
		self.nombre_slug = slugify(self.nombre)
		super(self.__class__, self).save(*args, **kwargs)

	def get_canciones(self):
		return Cancion.objects.filter(album=self)

	def get_numero_canciones(self):
		return len(Cancion.objects.filter(album=self))

	def get_duracion_album(self):
		duracion = 0
		for cancion in self.get_canciones():
			duracion += cancion.duracion
		return time.strftime("%H:%M:%S", time.gmtime(duracion))

	def __unicode__(self):
		return smart_unicode(self.nombre)

class Cancion(models.Model):
	nombre = models.CharField(max_length=50)
	nombre_slug = models.SlugField(max_length=50, blank=True, null=True)
	duracion = models.IntegerField()
	album = models.ForeignKey(Album, blank=True, null=True)
	artista = models.ForeignKey(Artista, blank=True, null=True)
	calificacion = models.PositiveIntegerField(default=0)

	def save(self, *args, **kwargs):
		self.nombre_slug = slugify(self.nombre)
		if(self.artista==None and self.album!=None):
			self.artista=self.album__artista
		super(self.__class__, self).save(*args, **kwargs)

	def get_duracion(self):
		return time.strftime("%M:%S", time.gmtime(self.duracion))

	def __unicode__(self):
		return smart_unicode(self.nombre)