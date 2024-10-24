from django.db import models
from bas.models import *
from pro.models import Categoria
from django.utils import timezone

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

#Seccion1 Web
class SeccionWeb1(models.Model):
    breadcrumb= models.CharField(max_length=255)
    titulo= models.CharField(max_length=255)
    boton= models.CharField(max_length=255)
    urlBoton=models.URLField(blank=True, null=True)
    tituloDescripcion= models.TextField(blank=True, null=True)
    descripcion= models.TextField(blank=True, null=True)
    imagen= models.ImageField(upload_to='seccion1/', blank=True, null=True)

    def __str__(self):
        return f"{self.titulo}"
    
#Seccion2 Web
class SeccionWeb2(models.Model):
    breadcrumb= models.CharField(max_length=255)
    titulo= models.CharField(max_length=255)
    tituloDescripcion= models.TextField(blank=True, null=True)
    categorias = models.ManyToManyField(Categoria, related_name='categorias')

    def __str__(self):
        return f"{self.titulo}"
    
#Seccion3 Web
class SeccionWeb3(models.Model):
    #titulos
    breadcrumb= models.CharField(max_length=255)
    titulo= models.CharField(max_length=255)

    #Contador 1
    tituloContador1= models.CharField(max_length=255)
    contador1= models.IntegerField()

    #Contador 2
    tituloContador2= models.CharField(max_length=255)
    contador2= models.IntegerField()

    #Contador 3
    tituloContador3= models.CharField(max_length=255)
    contador3= models.IntegerField()

    #banner1
    contadorImg1= models.IntegerField()
    tituloImg1= models.CharField(max_length=255)
    descripcionImg1= models.CharField(max_length=255)
    imagen1= models.ImageField(upload_to='bannerSeccion4/', blank=True, null=True)

    #banner2
    contadorImg2= models.IntegerField()
    tituloImg2= models.CharField(max_length=255)
    descripcionImg2= models.CharField(max_length=255)
    imagen2= models.ImageField(upload_to='bannerSeccion4/', blank=True, null=True)

    #banner3
    contadorImg3= models.IntegerField()
    tituloImg3= models.CharField(max_length=255)
    descripcionImg3= models.CharField(max_length=255)
    imagen3= models.ImageField(upload_to='bannerSeccion4/', blank=True, null=True)

    #banner4
    contadorImg4= models.IntegerField()
    tituloImg4= models.CharField(max_length=255)
    descripcionImg4= models.CharField(max_length=255)
    imagen4= models.ImageField(upload_to='bannerSeccion4/', blank=True, null=True)

    def __str__(self):
        return f"{self.titulo}"    
    
#Seccion4 Web
class SeccionWeb4(models.Model):
    #titulos
    breadcrumb= models.CharField(max_length=255)
    titulo= models.CharField(max_length=255)

#Seccion5 Web
class SeccionWeb5(models.Model):
    #titulos
    breadcrumb= models.CharField(max_length=255)
    titulo= models.CharField(max_length=255)
    #Imagenes
    imagen1= models.ImageField(upload_to='bannerSeccion5/', blank=True, null=True)
    imagen2= models.ImageField(upload_to='bannerSeccion5/', blank=True, null=True)

    #Card1
    imageCard1= models.ImageField(upload_to='bannerSeccion5/', blank=True, null=True)
    tituloCard1= models.CharField(max_length=255)
    precioCard1= models.IntegerField()
    boton1= models.CharField(max_length=255)

    #Card2
    imageCard2= models.ImageField(upload_to='bannerSeccion5/', blank=True, null=True)
    tituloCard2= models.CharField(max_length=255)
    precioCard2= models.IntegerField()
    boton2= models.CharField(max_length=255)

    #Card3
    imageCard3= models.ImageField(upload_to='bannerSeccion5/', blank=True, null=True)
    tituloCard3= models.CharField(max_length=255)
    precioCard3= models.IntegerField()
    boton3= models.CharField(max_length=255)

    def __str__(self):
        return f"{self.titulo}"
    
#Seccion6 Web
class SeccionWeb6(models.Model):
    #titulos
    breadcrumb= models.CharField(max_length=255)
    titulo= models.CharField(max_length=255)
    descripcion= models.TextField(blank=True, null=True)
    imagen= models.ImageField(upload_to='bannerSeccion5/', blank=True, null=True)
    boton= models.CharField(max_length=255)

    def __str__(self):
        return f"{self.titulo}"    
    
#Seccion Testimonios
class Testimonio(models.Model):
    nombre_cliente = models.CharField(max_length=255)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f'Testimonio de {self.nombre_cliente}'

#Seccion7 Web
class SeccionWeb7(models.Model):
    #titulos
    breadcrumb= models.CharField(max_length=255)
    titulo= models.CharField(max_length=255)
    testimonio = models.ManyToManyField(Testimonio, related_name='testimonios')
    imagen= models.ImageField(upload_to='seccion7/', blank=True, null=True)

    def __str__(self):
        return f"{self.titulo}"        
    
#Seccion8 Web
class SeccionWeb8(models.Model):
    #titulos
    breadcrumb= models.CharField(max_length=255)
    titulo= models.CharField(max_length=255)
    boton= models.CharField(max_length=255)
    bg= models.ImageField(upload_to='bannerSeccion8/', blank=True, null=True)

    #banner1
    contadorImg1= models.IntegerField()
    tituloImg1= models.CharField(max_length=255)
    descripcionImg1= models.CharField(max_length=255)
    imagen1= models.ImageField(upload_to='bannerSeccion8/', blank=True, null=True)
    boton1= models.CharField(max_length=255)

    #banner2
    contadorImg2= models.IntegerField()
    tituloImg2= models.CharField(max_length=255)
    descripcionImg2= models.CharField(max_length=255)
    imagen2= models.ImageField(upload_to='bannerSeccion8/', blank=True, null=True)
    boton2= models.CharField(max_length=255)

    #banner3
    contadorImg3= models.IntegerField()
    tituloImg3= models.CharField(max_length=255)
    descripcionImg3= models.CharField(max_length=255)
    imagen3= models.ImageField(upload_to='bannerSeccion8/', blank=True, null=True)
    boton3= models.CharField(max_length=255)

    #banner4
    contadorImg4= models.IntegerField()
    tituloImg4= models.CharField(max_length=255)
    descripcionImg4= models.CharField(max_length=255)
    imagen4= models.ImageField(upload_to='bannerSeccion8/', blank=True, null=True)
    boton4= models.CharField(max_length=255)

    def __str__(self):
        return f"{self.titulo}"  

#Logos
class Logo(models.Model):
    nombre_empresa = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='logos/')
    url_empresa = models.URLField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_empresa

#Seccion9 Web
class SeccionWeb9(models.Model):
    #titulos
    breadcrumb= models.CharField(max_length=255)
    titulo= models.CharField(max_length=255)
    logo = models.ManyToManyField(Logo, related_name='logos')

    def __str__(self):
        return f"{self.titulo}"                          