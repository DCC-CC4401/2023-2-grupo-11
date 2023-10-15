from django import forms
from django.utils import timezone
from perfil_apagno_app.models import nuevoEvento



class NuevoEventoForm(forms.ModelForm):
    class Meta:
        model = nuevoEvento
        #fields = "__all__"
        fields = ['nombre', 'host', 'fecha', 'hora', 'lugar', 'descripcion', 'categoria', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'host': forms.TextInput(attrs={'class':'form-control'}),
            'fecha': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'hora': forms.TimeInput(attrs={'class':'form-control', 'type':'time'}),
            'lugar': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.TextInput(attrs={'class':'form-control'}),
            'imagen': forms.FileInput(attrs={'class':'form-control'}),
        }
    #categoria = forms.ModelChoiceField(queryset=Categoria.objects.all()