from django import forms
from .models import Cargo, User

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['nombre']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'image', 'identificacion', 'telefono', 'direccion', 'cargo']        