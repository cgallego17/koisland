from django.views.generic import ListView
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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

#Guardar Producto
@login_required(login_url='bases:login')
def ProdAdd(request):
    contexto = {}
    if request.method == "POST":
        imagen=request.FILES['imagen_principal']
        dis = request.POST.get('disponible') == 'True'

        producto=Producto.objects.create(
            nombre = request.POST['nombre'].upper(),
            sku = request.POST['sku'],
            categoria = Categoria.objects.get(id=request.POST['categoria']),
            descripcion = request.POST['descripcion'],
            precio = request.POST['precio'],
            marca = Marca.objects.get(id=request.POST['marca']),
            modelo = request.POST['modelo'].upper(),
            dimensiones = request.POST['dimensiones'].upper(),
            peso = request.POST['peso'],
            stock = request.POST['stock'],
            imagen_principal = imagen,
            disponible=dis
        )

        if producto:
            messages.success(request, 'Exito al crear producto')
            return redirect("pro:producto_list")
        
        if not producto:
            messages.error(request, 'Error al crear producto')

    return render(request, contexto)

#Editar Producto 
@login_required(login_url='bases:login')
def ProdEdit(request, id):
    # Obtener el producto que se va a editar
    producto = get_object_or_404(Producto, id=id)
    
    if request.method == "POST":
        imagen = request.FILES.get('imagen_principal', producto.imagen_principal)
        dis = request.POST.get('disponible') == 'True'

        try:
            producto.nombre = request.POST['nombre'].upper()
            producto.sku = request.POST['sku']
            producto.categoria = Categoria.objects.get(id=request.POST['categoria'])
            producto.descripcion = request.POST['descripcion']
            producto.precio = request.POST['precio']
            producto.marca = Marca.objects.get(id=request.POST['marca'])
            producto.modelo = request.POST['modelo'].upper()
            producto.dimensiones = request.POST['dimensiones'].upper()
            producto.peso = request.POST['peso']
            producto.stock = request.POST['stock']
            producto.imagen_principal = imagen
            producto.disponible = dis
            
            producto.save()  # Guardar los cambios
            
            messages.success(request, 'Producto actualizado con éxito')
            return redirect("pro:producto_list")
        except Exception as e:
            messages.error(request, f'Error al actualizar el producto: {str(e)}')
    
    contexto = {
        'producto': producto
        # Incluir otros datos necesarios para el template, como listas de categorías y marcas
    }
    
    return render(request, "producto_edit.html", contexto)