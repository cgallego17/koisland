# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from bas.models import *

# Cargo en empresa
class Cargo(ClaseModelo):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return '{}'.format(self.nombre)

# Usuarios
class User(AbstractUser):
    image = models.ImageField(upload_to='img-users/', blank=True, null=True)
    identificacion = models.IntegerField(default=0, blank=True, null=True)
    telefono = models.IntegerField(default=0, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, blank=True, null=True)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url  