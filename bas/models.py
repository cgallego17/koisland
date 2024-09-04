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
    
    def save(self, *args, **kwargs):
        # Si hay una imagen, redimensionarla
        if self.imagen:
            self.imagen = self.resize_image(self.imagen)
        super().save(*args, **kwargs)

    def resize_image(self, image):
        # Abrir la imagen usando Pillow
        img = Image.open(image)
        img = img.convert('RGB')  # Asegurarse de que la imagen esté en formato RGB

        # Redimensionar la imagen
        img = img.resize((1100, 1100), Image.ANTIALIAS)

        # Guardar la imagen en memoria
        image_io = io.BytesIO()
        img.save(image_io, format='JPEG', quality=90)  # Puedes cambiar el formato y la calidad según tus necesidades
        image_file = InMemoryUploadedFile(image_io, 'ImageField', f"{self.nombre}.jpg", 'image/jpeg', image_io.getbuffer().nbytes, None)

        return image_file

# modelo de galeria
class ImageGallery(ClaseModelo):
    album = models.ForeignKey(AlbumGallery, related_name='imagenes', on_delete=models.CASCADE, verbose_name="Álbum")
    titulo = models.CharField(max_length=100, verbose_name="Título de la Imagen")
    imagen = models.ImageField(upload_to='imagenes/album/imagenes/', verbose_name="Imagen")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    iframe_code = models.TextField(blank=True, null=True, verbose_name="Código del Iframe del Video")

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        # Si hay una imagen, redimensionarla
        if self.imagen:
            self.imagen = self.resize_image(self.imagen)
        super().save(*args, **kwargs)

    def resize_image(self, image):
        # Abrir la imagen usando Pillow
        img = Image.open(image)
        img = img.convert('RGB')  # Asegurarse de que la imagen esté en formato RGB

        # Redimensionar la imagen
        img = img.resize((1100, 1100), Image.ANTIALIAS)

        # Guardar la imagen en memoria
        image_io = io.BytesIO()
        img.save(image_io, format='JPEG', quality=90)  # Puedes cambiar el formato y la calidad según tus necesidades
        image_file = InMemoryUploadedFile(image_io, 'ImageField', f"{self.titulo}.jpg", 'image/jpeg', image_io.getbuffer().nbytes, None)

        return image_file