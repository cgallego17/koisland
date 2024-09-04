from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import UpdateView
from django.http import Http404
from .models import *
from .forms import *
from pro.models import Producto

#Dashboard
@login_required(login_url='bas:login')
def home(request):
    cantidad_productos_activos = Producto.objects.filter(disponible=True).count()

    contexto = {
        'cantidad_productos_activos': cantidad_productos_activos,
    }


    return render(request, 'inicio_admin.html', contexto)

#Editar Empresa
@login_required(login_url='bas:login')
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

class CrearObjetoView(CreateView):
    login_url = 'bas:login'
    template_name = 'crear_objeto.html'
    model = None  

    def __init__(self, model, **kwargs):
        self.model = model
        super().__init__(**kwargs)

    def get_form_class(self):
        return objeto_form_factory(self.model)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name
        return context

    def get_success_url(self):
        return_url = self.kwargs['return_url']
        messages.success(self.request, f'{self.object} Fue creado con éxito ')
        return reverse(return_url)

class EditarObjetoView(UpdateView):
    login_url = 'bas:login'
    template_name = 'editar_objeto.html'
    model = None  

    def __init__(self, model, **kwargs):
        self.model = model
        super().__init__(**kwargs)

    def get_form_class(self):
        return objeto_form_factory(self.model)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name
        return context

    def get_object(self, queryset=None):
        try:
            obj = super().get_object(queryset)
            return obj
        except self.model.DoesNotExist:
            raise Http404('El objeto no existe')

    def get_success_url(self):
        return_url = self.kwargs['return_url']
        messages.success(self.request, f'{self.object} Fue editado con éxito ')
        return reverse(return_url)

class EliminarObjetoView(DeleteView):
    login_url = 'bas:login'
    template_name = 'eliminar_objeto.html'

    def __init__(self, **kwargs):
        self.model = kwargs.pop('model')
        super().__init__(**kwargs)

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name
        context['cancel_url'] = reverse(self.kwargs['return_url'])
        return context

    def get_success_url(self):
        return_url = self.kwargs['return_url']
        messages.success(self.request, f'{self.object} Fue eliminado con éxito')
        return reverse(return_url)

#Galeria
@login_required(login_url='bas:login')
def albumesView(request):
    albumes=AlbumGallery.objects.filter(estado=True)

    contexto = {
        'albumes': albumes,
    }

    return render(request, 'albumes.html', contexto)

#Album detalle
@login_required(login_url='bas:login')
def album_detail(request, id):
    imagenes = ImageGallery.objects.filter(album=id)

    return render(request, 'album_detail.html', {'imagenes': imagenes})