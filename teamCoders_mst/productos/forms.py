from django import forms

from .models import Producto
from .models import Contacto



class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio','imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Fruto'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            
        }
        labels = {
            'nombre':'', 'descripción':'','precio':'', 'imágen': ''
        }


class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        #fields = ["nombre", "correo", "correo", "tipoConsulta", "mensaje", "avisos"]
        fields = '__all__'
