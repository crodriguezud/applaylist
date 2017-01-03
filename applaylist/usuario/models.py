from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import user

from playlist.models import Cancion 

# Create your models here.

class Usuario(models.Model):
	usuario = models.OneToOneField(User)
	descripcion = models.TextField(blank=True, null=True)

	class Meta:
        verbose_name = _('Usuario')
        verbose_name_plural = _('Usuarios')

    def __unicode__(self):
        return str(self.usuario)

class PlayList(models.Model):
	creador = models.ForeignKey(User)
	nombre = models.CharField(max_length=50)
	caciones = models.ManyToManyField(Cancion)