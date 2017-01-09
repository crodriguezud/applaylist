from celery.decorators import task
from django.template import loader
from django.conf import settings
from django.core.mail import send_mail

CORREO_TEMPLATE = 'correo.txt'
ASUNTO_TEMPLATE = 'asunto.txt'

#Metodo para el envio de correos de notificacion
@task(name="enviar_correo_task")
def enviar_correo_task(nombre, playlist, correo):
    context = {
        'user': nombre,
        'playlist': playlist,
    }
    body = loader.render_to_string(CORREO_TEMPLATE, context).strip()
    subject = loader.render_to_string(ASUNTO_TEMPLATE, context).strip()
    send_mail(subject, body, 'info@applylist.com',
              [correo])
    return 'Se ha enviado el correo de notificacio exitosamente'
