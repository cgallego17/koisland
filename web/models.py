from django.db import models
from bas.models import *

# modelo de banners
class Web(ClaseModelo):
    titulo = models.CharField(max_length=100, verbose_name="Título de la Web")
    

# modelo de banners
class Banners(ClaseModelo):
    titulo = models.CharField(max_length=100, verbose_name="Título de la Imagen")
    imagen = models.ImageField(upload_to='imagenes/album/imagenes/', verbose_name="Imagen")

    def __str__(self):
        return self.titulo

