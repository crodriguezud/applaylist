from django.contrib.auth.decorators import login_required

from django.conf.urls import url

# Import Class Based Views
from .views import UsuarioView

urlpatterns = [
    url(r'^$', login_required(UsuarioView.as_view()), name='user_profile'),
    ]
