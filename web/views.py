from django.shortcuts import render
from .models import *

#Inicio pagina web
def inicio(request):

    men = Menu.objects.all()
    pro = Proyectos.objects.all()

    context={
        'menus': men,
        'proyectos': pro
    }

    return render(request, 'inicio.html', context)