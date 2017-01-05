from celery.decorators import task
from django.template import loader
from django.conf import settings
from django.core.mail import send_mail

#Metodo para el envio de correos de notificacion
@task(name="enviar_correo_task")
def enviar_correo_task(nombre, playlist, correo):
    body = [nombre],' has creado una nueva PlayList de nombre ',[playlist]
    subject = 'Nueva PlayList creada con ApPlyList'
    send_mail(subject, body, 'info@applylist.com',
              [correo])
    return 'Se ha enviado el correo de notificacio exitosamente'
