from django import forms
from .models import Transaccion, Cliente, Cierre

class TransaccionForm(forms.ModelForm):
    opciones = [('ingresar','ingresar'),('egresar','egresar')]
    tipo = forms.ChoiceField(widget=forms.Select, choices=opciones)
    class Meta:
        model = Transaccion
        fields = [
            'cliente',
            'valor',
            'tipo'
        ]

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'id_usuario',
            'apellido',
            'nombre',
            'telefono',
            'mail',
            'saldo'
        ]

class CierreForm(forms.ModelForm):
    class Meta:
        model = Cierre
        fields = [
            'valor'
        ]
