from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

#Categorias Articulos
@login_required(login_url='bas:login')
def CategoriasArticulos(request):
    categorias = CateArt.objects.all()

    return render(request, 'categoria_articulos_list.html', {'categorias': categorias})

#Articulos
@login_required(login_url='bas:login')
def Articulos(request):
    articulos = Articulo.objects.all()

    return render(request, 'articulos_list.html', {'articulos': articulos})