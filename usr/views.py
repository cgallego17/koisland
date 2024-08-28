from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import *
from .forms import *

#Cargos Usuarios
class CargoListView(ListView):
    model = Cargo
    template_name = 'cargo_list.html'
    context_object_name = 'cargos'

    def get_queryset(self):
        return super().get_queryset().order_by('-id')

#Usuarios
class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'