from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Artista(models.Model):
	nombre = models.CharField(max_length=60)
	

	def __unicode__(self):
        return smart_unicode(self.nombre)

class Album(models.Model):
	nombre = models.CharField(max_length=60)
	artista = models.ForeignKey(Artista)

	def __unicode__(self):
        return smart_unicode(self.nombre)

class Cancion(models.Model):
	nombre = models.CharField(max_length=60)
	duracion = model.IntegerField()
	album = models.ForeignKey(Album)

	def __unicode__(self):
        return smart_unicode(self.nombre)