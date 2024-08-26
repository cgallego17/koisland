from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

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
class Empresa(models.Model):

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
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.nombre)