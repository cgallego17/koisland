from django.db import models
from bas.models import *

#Menus Web
class Menu(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del menú
    url = models.URLField(blank=True, null=True)  # URL a la que el menú apunta
    orden = models.PositiveIntegerField(default=0)  # Para definir el orden del menú
    visible = models.BooleanField(default=True)  # Si el menú es visible o no

    class Meta:
        ordering = ['orden']  # Ordenar los menús por el campo 'orden'

    def __str__(self):
        return self.nombre

# modelo de banners
class Web(ClaseModelo):
    titulo = models.CharField(max_length=100, verbose_name="Título de la Web")

# modelo de banners
class Banners(ClaseModelo):
    titulo = models.CharField(max_length=100, verbose_name="Título de la Imagen")
    imagen = models.ImageField(upload_to='imagenes/album/imagenes/', verbose_name="Imagen")

    def __str__(self):
        return self.titulo

class Proyectos(models.Model):
    nombre = models.CharField(max_length=255)  # Nombre del proyecto
    descripcion = models.TextField(blank=True, null=True)  # Descripción detallada del proyecto
    fecha_inicio = models.DateField()  # Fecha de inicio del proyecto
    fecha_fin = models.DateField()  # Fecha de finalización del proyecto
    resultados = models.TextField(blank=True, null=True)  # Resultados obtenidos con el proyecto
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Presupuesto utilizado
    imagenes = models.ImageField(upload_to='proyectos/', blank=True, null=True)  # Galería de imágenes asociadas al proyecto
    archivos = models.FileField(upload_to='proyectos/archivos/', blank=True, null=True)  # Archivos adjuntos relevantes del proyecto

    class Meta:
        ordering = ['fecha_fin']  # Ordena los proyectos por la fecha de finalización
    
    def __str__(self):
        return f"{self.nombre}"    