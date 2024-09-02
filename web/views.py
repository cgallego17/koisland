from django.shortcuts import render

# Inicio web 
def inicio(request):
    
    return render(request, 'inicio.html')