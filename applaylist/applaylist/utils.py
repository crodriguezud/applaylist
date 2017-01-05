from pusher import Pusher
import os
#Configuracion Pusher

class Singleton(object):
  _instance = None
  def __new__(class_, *args, **kwargs):
    if not isinstance(class_._instance, class_):
        class_._instance = object.__new__(class_, *args, **kwargs)
    return class_._instance

class ClientePusher(Singleton, Pusher):

	def __init__(self):
		Pusher.__init__(self, app_id=os.environ['PUSH_APP_ID'], key=os.environ['PUSH_KEY'], secret=os.environ['PUSH_SECRET'], ssl=True)


cliente_pusher = ClientePusher()
