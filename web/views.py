from django.shortcuts import render

#Inicio pagina web
def inicio(request):

    return render(request, 'inicio.html')