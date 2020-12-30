from django.contrib import admin
from .models import  Cliente, Transaccion, Cierre

# Register your models here.
admin.site.register(Cierre)
admin.site.register(Cliente)
admin.site.register(Transaccion)

