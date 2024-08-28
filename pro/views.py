from django.views.generic import ListView
from .models import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria_list.html'
    paginate_by = 10  # número de categorías por página

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Categorías'
        return context

class MarcasListView(ListView):
    model = Marca
    template_name = 'marcas_list.html'
    paginate_by = 10  # número de productos por página

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de marcas'
        return context

class ProductoListView(ListView):
    model = Producto
    template_name = 'productos_list.html'
    paginate_by = 10  # número de productos por página

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Productos'
        return context    

@login_required(login_url='bases:login')
def ProdViewNew(request):
    template_name="producto_new.html"
    marcas=Marca.objects.all()
    categorias=Categoria.objects.all()

    context={
        'request':request,
        'marcas':marcas,
        'categorias':categorias,
    }

    return render(request,template_name,context)