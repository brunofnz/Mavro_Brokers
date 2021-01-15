from django.db import models



# Create your models here.
class Cliente(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    apellido = models.CharField(max_length= 50, blank=True, null=True)
    nombre = models.CharField(max_length= 50, blank=True, null=True)
    telefono = models.CharField(max_length= 50, blank=True, null=True)
    mail = models.CharField(max_length= 50, blank=True, null=True)
    saldo = models.IntegerField(max_length= 50, blank=True, null=True)
    fecha_alta = models.DateField(auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombre']

    def __str__(self):
        return "{}, {}".format(self.apellido,self.nombre)

class Transaccion(models.Model):
    id_transaccion = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor = models.IntegerField(max_length= 50, blank=True, null=True)
    tipo = models.CharField(max_length= 50, blank=True, null=True)
    fecha_alta = models.DateField(auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'Transaccion'
        verbose_name_plural = 'Transacciones'
        ordering = ['id_transaccion']

    def __str__(self):
        return "{} \t|\t {} \t|\t {}".format(self.id_transaccion,self.tipo,self.cliente)

class Cierre(models.Model):
    id_cierre = models.AutoField(primary_key=True)
    valor = models.CharField(max_length= 50, blank=True, null=True)
    fecha_alta = models.DateField(auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'Cierre'
        verbose_name_plural = 'Cierres'
        ordering = ['fecha_alta']

    def __str__(self):
        return "{} \t|\t {} \t|\t {}".format(self.id_cierre,self.fecha_alta,self.valor)
