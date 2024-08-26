from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    # Información básica
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    
    # Relación con categorías
    categoria = models.ForeignKey(Categoria, related_name='productos', on_delete=models.CASCADE)

    # Atributos generales para diferentes tipos de productos
    marca = models.CharField(max_length=100, blank=True, null=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    dimensiones = models.CharField(max_length=100, blank=True, null=True, help_text="Dimensiones del producto")
    peso = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text="Peso en kg")
    material = models.CharField(max_length=100, blank=True, null=True)
    
    # Información específica para peces
    nombre_cientifico = models.CharField(max_length=200, blank=True, null=True)
    tamano_maximo = models.DecimalField(max_digits=5, decimal_places=2, help_text="Tamaño máximo en cm", blank=True, null=True)
    temperatura_recomendada = models.CharField(max_length=50, help_text="Rango de temperatura en °C", blank=True, null=True)
    ph_recomendado = models.CharField(max_length=50, help_text="Rango de pH", blank=True, null=True)
    dieta = models.CharField(max_length=200, blank=True, null=True)
    cuidados_especiales = models.TextField(blank=True, null=True)
    
    # Información específica para equipos y accesorios
    tipo_equipo = models.CharField(max_length=100, blank=True, null=True, help_text="Tipo de equipo (ej. filtro, bomba)")
    capacidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Capacidad del equipo (ej. litros por hora)")
    uso_recomendado = models.TextField(blank=True, null=True, help_text="Descripción de uso recomendado")
    
    # Información de imágenes
    imagen_principal = models.ImageField(upload_to='productos/', blank=True, null=True)
    imagenes_adicionales = models.ManyToManyField('Imagen', blank=True)
    
    # Estado del producto
    disponible = models.BooleanField(default=True)
    
    # Información de seguimiento
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

class Imagen(models.Model):
    imagen = models.ImageField(upload_to='productos/')
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.descripcion or "Imagen"