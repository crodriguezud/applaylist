# encoding:utf-8
import time
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
from django.template.defaultfilters import slugify

from playlist.models import Cancion 
from .tasks import enviar_correo_task
from applaylist.utils import cliente_pusher


# Create your models here.

class Usuario(models.Model):
	usuario = models.OneToOneField(User)
	descripcion = models.TextField(blank=True, null=True)

	def get_creador_playlist(self):
		return PlayList.objects.filter(creador=self.usuario)

	class Meta:
		verbose_name = _('Usuario')
		verbose_name_plural = _('Usuarios')
	
	def __unicode__(self):
		return str(self.usuario)

class PlayList(models.Model):
	creador = models.ForeignKey(User)
	nombre = models.CharField(max_length=50, blank=True, null=True)
	nombre_slug = models.SlugField(max_length=50, blank=True, null=True)
	caciones = models.ManyToManyField(Cancion)

	def save(self, *args, **kwargs):
		cliente_pusher.trigger('ApPlayList', 'Creacion PlayList', {'name': self.nombre})
		self.nombre_slug = slugify(self.nombre)
		super(self.__class__, self).save(*args, **kwargs)

	def get_duracion_playlist(self):
		duracion = 0
		for cancion in self.caciones.all():
			duracion += cancion.duracion
		return time.strftime("%H:%M:%S", time.gmtime(duracion))
	
	def get_numero_canciones(self):
		return len(self.caciones.all())

	def __unicode__(self):
		return str(self.nombre)

'''
Creacion referencia a Usuario
'''

def crear_perfil(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        profile = Usuario()
        profile.user = user
        profile.save()

post_save.connect(crear_perfil, sender=User)


'''
Envio de correo luego de crear PlayList
'''

def enviar_notificacion(sender, **kwargs):
    playlist = kwargs["instance"]
    enviar_correo_task.delay(playlist.creador.username, playlist.nombre, playlist.creador.email)

post_save.connect(enviar_notificacion, sender=PlayList)