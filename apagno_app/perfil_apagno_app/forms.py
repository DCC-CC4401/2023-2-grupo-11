from django import forms
from django.utils import timezone
from perfil_apagno_app.models import *

# Si la pagina no quiere iniciar por Categoria, eliminar esto y actualizar pagina
# Funcion util para invocar las categorias al momento de seleccionarlas en el formulario del evento
cats = Categorias.objects.all().values_list('nombre', 'nombre')
cats_list = []
for item in cats:
    cats_list.append(item)

# class NuevoEventoForm señala el formato del formulario para un evento nuevo
class NuevoEventoForm(forms.ModelForm):
    class Meta:
        model = nuevoEvento
        fields = ['nombre', 'host', 'fecha', 'hora', 'lugar', 'descripcion', 'categoria', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'host': forms.TextInput(attrs={'class':'form-control'}),
            'fecha': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'hora': forms.TimeInput(attrs={'class':'form-control', 'type':'time'}),
            'lugar': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            #'categoria': forms.Select(attrs={'class':'form-control'}),
            'categoria': forms.Select(choices=cats_list,attrs={'class':'form-control'}),
            'imagen': forms.FileInput(attrs={'class':'form-control'}),
        }

# for user update en profile
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','nickname','pronouns','email','contact']

# for profile update
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar'] 