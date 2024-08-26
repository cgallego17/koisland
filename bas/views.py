from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

#Dashboard
def home(request):
    return render(request, 'base/index.html')


#Editar Empresa
def empresa_edit(request):
    empresa = Empresa.objects.first()  
    if not empresa:
        return redirect('bas:admin_home')  
    if request.method == 'POST':
        form = EmpresaForm(request.POST, request.FILES, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('empresa_edit')  
    else:
        form = EmpresaForm(instance=empresa)
    
    return render(request, 'empresa_edit.html', {'form': form})