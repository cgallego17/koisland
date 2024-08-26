from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib import messages

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
            messages.success(request, 'Empresa editada con éxito.')
            return redirect('bas:empresa_edit')  
    else:
        form = EmpresaForm(instance=empresa)
    
    return render(request, 'empresa_edit.html', {'form': form})