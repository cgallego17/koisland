from django.db import models
from django.contrib.auth.models import User
from bas.models import *

class Categoria(ClaseModelo):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='productos/categorias/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Marca(ClaseModelo):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='productos/marcas/', blank=True, null=True)

    def __str__(self):
        return self.nombre    

class Producto(ClaseModelo):
    # Información básica
    nombre = models.CharField(max_length=200)
    sku = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    
    # Relación con categorías
    categoria = models.ForeignKey(Categoria, related_name='productos', on_delete=models.CASCADE)

    # Atributos generales para diferentes tipos de productos
    marca = models.ForeignKey(Marca, related_name='productos', on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    dimensiones = models.CharField(max_length=100, blank=True, null=True, help_text="Dimensiones del producto")
    peso = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text="Peso en kg")
 
    # Información de imágenes
    imagen_principal = models.ImageField(upload_to='productos/', blank=True, null=True)
    
    # Estado del producto
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Imagen(ClaseModelo):
    imagen = models.ImageField(upload_to='productos/')
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    producto = models.ForeignKey(Producto, related_name='productos', on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion or "Imagen"