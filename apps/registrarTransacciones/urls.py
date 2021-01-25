from django.contrib import admin
from django.urls import path
from .views import registrarTransaccion, listarTransacciones, registrarCliente, listarClientes, registrarCierre, listarCierres

urlpatterns = [
    path('Clientes/', listarClientes, name='listaClientes'),
    path('RegistrarCliente/', registrarCliente, name='registrarCliente'),
    path('Transacciones/', listarTransacciones, name='listaTransacciones'),
    path('RegistrarTransaccion/', registrarTransaccion, name='registrarTransaccion'),
    path('Cierres/', listarCierres, name='listaCierres'),
    path('RegistrarCierres/', registrarCierre, name='registrarCierre')
]