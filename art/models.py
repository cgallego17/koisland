from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from bas.models import *

#Categoria Articulo
class CateArt(ClaseModelo):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

#Articulo
class Articulo(ClaseModelo):
    ESTADOS = (
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
    )

    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='imagenes/articulos/', verbose_name="Imagen")
    contenido = models.TextField()
    categorias = models.ManyToManyField(CateArt, related_name='articulos')
    iframe_code = models.TextField(blank=True, null=True, verbose_name="Código del Iframe del Video")
    estadoArt = models.CharField(max_length=10, choices=ESTADOS, default='borrador')

    class Meta:
        ordering = ['-id']
        verbose_name = 'artículo'
        verbose_name_plural = 'artículos'

    def __str__(self):
        return self.titulo

    def publicar(self):
        self.estado = 'publicado'
        self.save()
