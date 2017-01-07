from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.models import User

class UsuarioView(DetailView):
    model = User
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        self.object = request.user
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)