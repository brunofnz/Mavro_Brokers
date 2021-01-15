from django import forms
from .models import Transaccion

class TransaccionForm(forms.ModelForm):
    opciones = [(1,'ingresar'),(2,'egresar')]
    tipo = forms.ChoiceField(widget=forms.Select, choices=opciones)
    class Meta:
        model = Transaccion
        fields = [
            'cliente',
            'valor',
            'tipo'
        ]
