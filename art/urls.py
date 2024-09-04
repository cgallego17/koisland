from django.urls import path, include
from .views import *
from bas.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    #Categorias
    path('categorias/art/', CategoriasArticulos, name='categorias_articulos'),
    path('categorias/art/crear/', CrearObjetoView.as_view(model=CateArt), name='crear_art', kwargs={'return_url': 'art:categorias_articulos'}),
    path('categorias/art/editar/<int:pk>/', EditarObjetoView.as_view(model=CateArt), name='editar_art', kwargs={'return_url': 'art:categorias_articulos'}),
    path('categorias/art/eliminar/<int:pk>/', EliminarObjetoView.as_view(model=CateArt), name='eliminar_art', kwargs={'return_url': 'art:categorias_articulos'}),

    #Articulos
    path('articulos/', Articulos, name='articulos'),
    path('articulos/crear/', CrearObjetoView.as_view(model=Articulo), name='crear_articulo', kwargs={'return_url': 'art:articulos'}),
    path('articulos/editar/<int:pk>/', EditarObjetoView.as_view(model=Articulo), name='editar_articulo', kwargs={'return_url': 'art:articulos'}),
    path('articulos/eliminar/<int:pk>/', EliminarObjetoView.as_view(model=Articulo), name='eliminar_articulo', kwargs={'return_url': 'art:articulos'}),
]