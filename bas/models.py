from django.db import models
from django.conf import settings
from PIL import Image
import io
from django.core.files.uploadedfile import InMemoryUploadedFile

# Clase Modelo.
class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, on_delete=models.DO_NOTHING, related_name='%(class)s_requests_created')
    um = models.IntegerField(blank=True,null=True)
    
    class Meta:
        abstract=True

#Empresa
class Empresa(ClaseModelo):
    # Fields
    nombre = models.CharField(max_length=250)
    telefono = models.IntegerField(blank=True, null=True)
    logo = models.ImageField(upload_to="upload/images/empresa", blank=True, null=True)
    web = models.URLField(blank=True, null=True)
    terminos = models.TextField(max_length=512, blank=True, null=True)
    nit = models.IntegerField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=250, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    whatsapp = models.IntegerField(blank=True, null=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.nombre)
    
# modelo de album de galeria
class AlbumGallery(ClaseModelo):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Álbum")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    imagen = models.ImageField(upload_to='imagenes/album/', verbose_name="Imagen")

    def __str__(self):
        return self.nombre

# modelo de galeria
class ImageGallery(ClaseModelo):
    album = models.ForeignKey(AlbumGallery, related_name='imagenes', on_delete=models.CASCADE, verbose_name="Álbum")
    titulo = models.CharField(max_length=100, verbose_name="Título de la Imagen")
    imagen = models.ImageField(upload_to='imagenes/album/imagenes/', verbose_name="Imagen")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    iframe_code = models.TextField(blank=True, null=True, verbose_name="Código del Iframe del Video")

    def __str__(self):
        return self.titulo