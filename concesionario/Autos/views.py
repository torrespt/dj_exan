from django.shortcuts import render

# Create your views here.
def inicio(request):
    contexto={}
    return render(request, 'inicio.html', contexto)
def Autos(request):
    prod=['Audi', 'Chevrolet','Chevrolet', 'Toyota','Mercedes']
    context={'listado':prod}
    return render(request, 'autos.html', context)

def clientes(request):
    prod=['Andres', 'David','Angel', 'Danny','Juan']
    context={'listado':prod}
    return render(request, 'clientes.html', context)
