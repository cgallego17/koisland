from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name="admin_home"),
    path('empresa/edit/', empresa_edit, name='empresa_edit'),

    #Album
    path('albumes/', albumesView, name='albumes'),
    path('album/detalle/<int:id>/', album_detail, name='albumes_detalle'),
    path('albumes/crear/', CrearObjetoView.as_view(model=AlbumGallery), name='crear_album', kwargs={'return_url': 'bas:albumes'}),
    path('albumes/<int:pk>/editar/', EditarObjetoView.as_view(model=AlbumGallery), name='editar_album', kwargs={'return_url': 'bas:albumes'}),
    path('albumes/<int:pk>/eliminar/', EliminarObjetoView.as_view(model=AlbumGallery), name='eliminar_album', kwargs={'return_url': 'bas:albumes'}),

    #Imagenes
    path('imagen/add/', CrearObjetoView.as_view(model=ImageGallery), name='add_image', kwargs={'return_url': 'bas:albumes'}),
    path('imagen/<int:pk>/editar/', EditarObjetoView.as_view(model=ImageGallery), name='editar_image', kwargs={'return_url': 'bas:albumes'}),
    path('imagen/<int:pk>/eliminar/', EliminarObjetoView.as_view(model=ImageGallery), name='eliminar_image', kwargs={'return_url': 'bas:albumes'}),





    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]