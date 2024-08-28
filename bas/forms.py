from django import forms
from .models import Empresa
from django.forms import ModelForm

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

#Creador de objetos
def objeto_form_factory(modelo):
    class ObjetoForm(forms.ModelForm):
        class Meta:
            model = modelo
            fields = '__all__'
            exclude = ['estado', 'uc', 'um', 'last_login', 'password', 'is_superuser', 'is_staff', 'is_active']
             
    return ObjetoForm