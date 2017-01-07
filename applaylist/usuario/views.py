from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.models import User
from .models import PlayList
from .forms import CrearPlayListForm, CrearCancionForm, AniadirCancionForm
from playlist.models import Cancion

class UsuarioView(DetailView):
    model = User
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        self.object = request.user
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

class CrearPlayListView(CreateView):
    template_name = 'crear_playlist.html'
    model = PlayList
    form_class = CrearPlayListForm

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.init_form_data(request.user)
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return '/user-profile/' + str(self.object.nombre_slug)

class PlayListView(DetailView):
    model = PlayList
    template_name = 'playlist.html'
    slug_url_kwarg = 'playlist_slug'
    slug_field = 'nombre_slug'

class CrearCancionView(CreateView):
    template_name = 'crear_cancion.html'
    model = Cancion
    form_class = CrearCancionForm

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return '/user-profile/'

class AniadirCancionView(UpdateView):
    model = PlayList
    template_name = 'aniadir_cancion.html'
    form_class = AniadirCancionForm
    slug_url_kwarg = 'playlist_slug'
    slug_field = 'nombre_slug'

    def get_success_url(self):
        return '/user-profile/'
