from django.shortcuts import render
from .models import *

#Inicio pagina web
def inicio(request):
    men = Menu.objects.all()
    pro = Proyectos.objects.all()
    Seccion1 = SeccionWeb1.objects.all().first()
    Seccion2 = SeccionWeb2.objects.all().first()
    Seccion3 = SeccionWeb3.objects.all().first()
    Seccion4 = SeccionWeb4.objects.all().first()
    Seccion5 = SeccionWeb5.objects.all().first()
    Seccion6 = SeccionWeb6.objects.all().first()
    Seccion7 = SeccionWeb7.objects.all().first()
    Seccion8 = SeccionWeb8.objects.all().first()
    Seccion9 = SeccionWeb9.objects.all().first()
    Seccion10 = SeccionWeb10.objects.all().first()
    logos = Logo.objects.all()

    #Galerias
    galeria= AlbumGallery.objects.all()
    #Categorias
    categoria = Categoria.objects.filter(estado=True)
    #Galeria Home
    galeriaHome= ImageGallery.objects.filter(album_id=5)
    #testimonio
    testimonios=Testimonio.objects.filter(activo=True)
    #Imagenes Ig
    imgIg= imagenesIg.objects.all()
    #Banners
    banners=Banners.objects.all()

    context={
        'menus': men,
        'proyectos': pro,
        'Seccion1': Seccion1,
        'Seccion2': Seccion2,
        'Seccion3': Seccion3,
        'Seccion3': Seccion3,
        'Seccion4': Seccion4,
        'Seccion5': Seccion5,
        'Seccion6': Seccion6,
        'Seccion7': Seccion7,
        'Seccion8': Seccion8,
        'Seccion9': Seccion9,
        'Seccion10': Seccion10,
        'testimonios': testimonios,
        'categoria': categoria,
        'galeria': galeria,
        'galeriaHome': galeriaHome,
        'logos': logos,
        'imgIg': imgIg,
        'banners': banners,
    }

    return render(request, 'inicio.html', context)