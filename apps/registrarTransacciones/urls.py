from django.contrib import admin
from django.urls import path
from .views import registrarTransaccion

urlpatterns = [
    path('RegistrarTransaccion/', registrarTransaccion, name='registrarTransaccion'),
]