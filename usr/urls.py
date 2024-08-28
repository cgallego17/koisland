from django.urls import path
from bas.views import *
from .views import *

urlpatterns = [
    # Cargos
    path('cargos/', CargoListView.as_view(), name='cargo_list'),
    path('cargos/crear/', CrearObjetoView.as_view(model=Cargo), name='crear_cargo', kwargs={'return_url': 'usr:cargo_list'}),
    path('cargos/<int:pk>/editar/', EditarObjetoView.as_view(model=Cargo), name='editar_cargo', kwargs={'return_url': 'usr:cargo_list'}),
    path('cargos/<int:pk>/eliminar/', EliminarObjetoView.as_view(model=Cargo), name='eliminar_cargo', kwargs={'return_url': 'usr:cargo_list'}),
    
    # Usuarios
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/editar/', EditarObjetoView.as_view(model=User), name='editar_user', kwargs={'return_url': 'usr:user_list'}),

]