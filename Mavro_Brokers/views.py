from django.shortcuts import render
from datetime import date
from datetime import datetime

def dashboard(request):
    return render(request, "dashboard.html")

def landingPage(request):
    return render(request, "landingPage.html")


class MB:
	transferencias=[]

class transferencia:
	idt=int
	valor=int
	tipo=str
	fecha=datetime.now()

sistema=MB

def nueva_transferencia(cliente, valor, tipo):
	nuevatransf=transferencia
	nuevatransf.idt=leng(sistema.transferencias)
	nuevatransf.valor=valor
	nuevatransf.tipo=tipo
	sistema.transferencias.Append(nuevatransf)


"""cliente=input("ingresar cliente")
valor=input("ingresar valor")
tipo=input("ingresar tipo de operacion")

nueva_transferencia(cliente, valor, tipo)

print(sistema.transferencias)"""