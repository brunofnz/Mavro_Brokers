from django.shortcuts import render, redirect
from .models import Transaccion, Cliente, Cierre
from .forms import TransaccionForm, ClienteForm, CierreForm
import sqlite3

# Create your views here.


con = sqlite3.connect('db.sqlite3', check_same_thread=False)

def registrarTransaccion(request):
    if request.method == 'POST':
        transaccion_form = TransaccionForm(request.POST)
        if transaccion_form.is_valid():
            print("Formulario valido")
            nombreApellido = limpiarApellidoNombre(str(transaccion_form.cleaned_data['cliente']))
            if transaccion_form.cleaned_data['tipo'] == "ingresar":
                print("tipo ingreso")
                ingresarMonto(con, nombreApellido[1], nombreApellido[0], transaccion_form.cleaned_data['valor'])
                print("se ingreso el monto")
                try:
                    transaccion_form.save()
                except(e):
                    print("hubo un error")
                    print(e)
            if transaccion_form.cleaned_data['tipo'] == "egresar":
                print("tipo egresar")
                egresarMonto(con, nombreApellido[1], nombreApellido[0], transaccion_form.cleaned_data['valor'])
                print("se egreso el monto")
                try:
                    transaccion_form.save()
                except(e):
                    print("hubo un error")
                    print(e)
            return redirect('listaTransacciones')
    else:
        print("NO POST")
        transaccion_form = TransaccionForm()
    return render(request,'registrarTransaccion.html',{'transaccion_form':transaccion_form})

def registrarCliente(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            print("Formulario valido")
            try:
                cliente_form.save()
            except(e):
                print("hubo un error")
                print(e)
        return redirect('listaClientes')
    else:
        print("NO POST")
        cliente_form = ClienteForm()
    return render(request,'registrarCliente.html',{'cliente_form':cliente_form})    

def ingresarMonto(con,nombre,apellido, valor):
    
    saldo = 0
    valor = int(valor)

    #aca se conecta y busca el saldo del cliente propuesto
    cursorObj = con.cursor()
    data = [(nombre),(apellido)]
    cursorObj.execute('SELECT saldo FROM registrarTransacciones_cliente WHERE nombre=(?) AND apellido=(?)', data)
    saldo = cursorObj.fetchall()
    
    #aca limpia el saldo extraido por que tieen basura y lo suma al valor dado
    #[('1500'),]
    saldo = limpiarSaldo(saldo)
    saldo = saldo + valor

    """cliente = Cliente(apellido,nombre,saldo)"""
    #en data se coloca las variables para lugo cargar en la base de datos
    data = [(saldo),(nombre),(apellido)]
    cursorObj.execute('UPDATE registrarTransacciones_cliente SET saldo=(?) WHERE nombre=(?) and apellido=(?)', data)
    con.commit()

def egresarMonto(con,nombre,apellido, valor):
    
    saldo = 0
    valor = int(valor)

    #aca se conecta y busca el saldo del cliente propuesto
    cursorObj = con.cursor()
    data = [(nombre),(apellido)]
    cursorObj.execute('SELECT saldo FROM registrarTransacciones_cliente WHERE nombre=(?) AND apellido=(?)', data)
    saldo = cursorObj.fetchall()
    
    #aca limpia el saldo extraido por que tieen basura y lo suma al valor dado
    #[('1500'),]
    saldo = limpiarSaldo(saldo)
    if saldo >= valor:
        saldo = saldo - valor
        """cliente = Cliente(apellido,nombre,saldo)"""
        #en data se coloca las variables para lugo cargar en la base de datos
        data = [(saldo),(nombre),(apellido)]
        cursorObj.execute('UPDATE registrarTransacciones_cliente SET saldo=(?) WHERE nombre=(?) and apellido=(?)', data)
        con.commit()

def limpiarSaldo(saldo):
    saldo = str(saldo)
    saldo = saldo.replace("[","")
    saldo = saldo.replace("(","")
    saldo = saldo.replace("'","")
    saldo = saldo.replace(",","")
    saldo = saldo.replace(")","")
    saldo = saldo.replace("]","")
    saldo = int(saldo)
    return saldo

def limpiarApellidoNombre(ApellidoNombre):
    apellido = ""
    nombre = ""
    condicion = True
    for caracter in ApellidoNombre:
        if caracter != "," and condicion:
            apellido = apellido + caracter + ""
        else:
            condicion = False
            nombre = nombre + caracter + ""
    nombre = nombre.replace(", ","")
    return apellido,nombre

def listarTransacciones(request):
    transacciones = Transaccion.objects.order_by('-id_transaccion')
    return render(request, 'listaTransacciones.html', {'transacciones': transacciones})

def listarClientes(request):
    clientes = Cliente.objects.order_by('apellido')
    return render(request, 'listaClientes.html', {'clientes': clientes})

def registrarCierre(request):
    if request.method == 'POST':
        cierre_form = CierreForm(request.POST)
        if cierre_form.is_valid():
            print("Formulario valido")
            try:
                cierre_form.save()
            except(e):
                print("hubo un error")
                print(e)
        return redirect('listaCierres')
    else:
        print("NO POST")
        cierre_form = CierreForm()
    return render(request,'registrarCierre.html',{'cierre_form':cierre_form})

def listarCierres(request):
    cierres = Cierre.objects.order_by('-id_cierre')
    return render(request, 'listaCierres.html', {'cierres': cierres})

