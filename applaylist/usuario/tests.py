from django.test import TestCase

from usuario.models import PlayList 

class PlayListTestCase(TestCase): 
	def setUp(self): 
		usuario = Usuario.objects.filter(usuario__username="crodriguez")
		PlayList.objects.create(user=usuario, nombre="lista de prueba", canciones="") 

	def test_nombre_lista(self): 
		lion = PlayList.objects.get(nombre="ista de prueba") 