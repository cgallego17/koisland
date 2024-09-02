from django.urls import path
from bas.views import *
from .models import *
from .views import *

urlpatterns = [
    # Categorias
    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/crear/', CrearObjetoView.as_view(model=Categoria), name='crear_categoria', kwargs={'return_url': 'pro:categoria_list'}),
    path('categorias/<int:pk>/editar/', EditarObjetoView.as_view(model=Categoria), name='editar_categoria', kwargs={'return_url': 'pro:categoria_list'}),
    path('categorias/<int:pk>/eliminar/', EliminarObjetoView.as_view(model=Categoria), name='eliminar_categoria', kwargs={'return_url': 'pro:categoria_list'}),

    #Marcas
    path('marcas/', MarcasListView.as_view(), name='marca_list'),
    path('marcas/crear/', CrearObjetoView.as_view(model=Marca), name='crear_marca', kwargs={'return_url': 'pro:marca_list'}),
    path('marcas/<int:pk>/editar/', EditarObjetoView.as_view(model=Marca), name='editar_marca', kwargs={'return_url': 'pro:marca_list'}),
    path('marcas/<int:pk>/eliminar/', EliminarObjetoView.as_view(model=Marca), name='eliminar_marca', kwargs={'return_url': 'pro:marca_list'}),

    # Productos
    path('productos/', ProductoListView.as_view(), name='producto_list'),
    path('producto/add/', ProdViewNew, name='producto_create'),
    path('producto/edit/<int:id>/', ProdEdit, name='producto_edit'),
    path('producto/form/add/', ProdAdd, name='producto_add'),
    path('productos/<int:pk>/eliminar/', EliminarObjetoView.as_view(model=Producto), name='eliminar_producto', kwargs={'return_url': 'pro:producto_list'}),

    #Anadir imagenes a productos
    path('producto/imagen/add/<int:id>/', asociarProductoImagen, name='producto_add_image'),
    path('producto/imagen/eliminar/<int:id>/', eliminarProductoImagen, name='producto_delete_image'),
]