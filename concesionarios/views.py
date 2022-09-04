from django.http import HttpResponse
from django.shortcuts import render
from .models import auto,sucursal,cliente
from django.template import Context,Template,loader
from concesionarios.forms import *
# Create your views here.

def concesionario(request):
    #Esto viene a ser la landing
    return render (request,"concesionario/template1.html")

#view para formulario con django
def clienteFormulario(request):
    if request.method=="POST":
        miFormularioc = ClienteFormulario(request.POST)
        print(miFormularioc)
        if miFormularioc.is_valid():
            info=miFormularioc.cleaned_data
            print(info)
            nombre=info.get("nombre")
            apellido=info.get("apellido")
            dni=info.get("dni")
            fecha_compra=info.get("fecha_compra")
            cliente1=cliente(nombre=nombre,apellido=apellido,dni=dni,fecha_compra=fecha_compra)
            cliente1.save()
            return render(request,"concesionario/template1.html",{"mensaje":"Cliente Creado"})
        else:
            return render(request,"concesionario/template1.html",{"mensaje":"Error en la carga"})
    else:
        miFormularioc=ClienteFormulario()
        return render(request,"concesionario/clienteFormulario.html",{"formulario":miFormularioc})
    
def autoFormulario(request):
    if request.method=="POST":
        miFormularioa = AutoFormulario(request.POST)
        print(miFormularioa)
        if miFormularioa.is_valid():
            info=miFormularioa.cleaned_data
            print(info)
            marca=info.get("marca")
            patente=info.get("patente")
            modelo=info.get("modelo")
            fecha_ing=info.get("fecha_ing")
            auto1=auto(marca=marca,patente=patente,modelo=modelo,fecha_ing=fecha_ing)
            auto1.save()
            return render(request,"concesionario/template1.html",{"mensaje":"Auto Creado"})
        else:
            return render(request,"concesionario/template1.html",{"mensaje":"Error en la carga"})
    else:
        miFormularioa=AutoFormulario()
        return render(request,"concesionario/autoFormulario.html",{"formulario":miFormularioa})

def sucursalFormulario(request):
    if request.method=="POST":
        miFormularios = SucursalFormulario(request.POST)
        print(miFormularios)
        if miFormularios.is_valid():
            info=miFormularios.cleaned_data
            print(info)
            provincia=info.get("provincia")
            localidad=info.get("localidad")
            empleados=info.get("empleados")
            fecha_inaugural=info.get("fecha_inaugural")
            sucursal1=sucursal(provincia=provincia,localidad=localidad,empleados=empleados,fecha_inaugural=fecha_inaugural)
            sucursal1.save()
            return render(request,"concesionario/template1.html",{"mensaje":"Sucursal Creada"})
        else:
            return render(request,"concesionario/template1.html",{"mensaje":"Error en la carga"})
    else:
        miFormularios=SucursalFormulario()
        return render(request,"concesionario/sucursalFormulario.html",{"formulario":miFormularios})

def buscar_sucursal(request):
    if request.GET["localidad"]:
        locali=request.GET["localidad"]
        sucursales=sucursal.objects.filter(localidad=locali)
        if len(sucursales)!=0:
            return render (request, "concesionario/resultadosBusquedaSucursal.html",{"sucursales":sucursales})
        else:
            return render (request, "concesionario/resultadosBusquedaSucursal.html",{"mensaje": "no hay una sucursal en esa localidad"})
    else:
        return render (request, "concesionario/busquedaSucursal.html",{"mensaje": "No ingresaste ningun dato"})

def buscar_cliente(request):
    if request.GET["dni"]:
        denei=request.GET["dni"]
        clientes=cliente.objects.filter(dni=denei)
        if len(clientes)!=0:
            return render (request, "concesionario/resultadosBusquedaCliente.html",{"clientes":clientes})
        else:
            return render (request, "concesionario/resultadosBusquedaCliente.html",{"mensaje": "no hay un cliente con ese DNI"})
    else:
        return render (request, "concesionario/busquedaCliente.html",{"mensaje": "No ingresaste ningun dato"})

def buscar_auto(request):
    if request.GET["patente"]:
        paten=request.GET["patente"]
        autos=auto.objects.filter(patente=paten)
        if len(autos)!=0:
            return render (request, "concesionario/resultadosBusquedaAuto.html",{"autos":autos})
        else:
            return render (request, "concesionario/resultadosBusquedaAuto.html",{"mensaje": "no hay un auto en con esa patente"})
    else:
        return render (request, "concesionario/busquedaAuto.html",{"mensaje": "No ingresaste ningun dato"}) 

def busquedaSucursal(request):
    return render(request,"concesionario/busquedaSucursal.html")

def busquedaCliente(request):
    return render(request,"concesionario/busquedaCliente.html")

def busquedaAuto(request):
    return render(request,"concesionario/busquedaAuto.html")

def leerAutos(request):
    autos=auto.objects.all()
    return render(request, "concesionario/leerAutos.html", {"autos":autos})

def leerClientes(request):
    clientes=cliente.objects.all()
    return render(request, "concesionario/leerClientes.html", {"clientes":clientes})

def leerSucursales(request):
    sucursales=sucursal.objects.all()
    return render(request, "concesionario/leerSucursales.html", {"sucursales":sucursales})

def eliminarAuto(request,id):
    autos=auto.objects.get(id=id)
    autos.delete()
    totalautos=auto.objects.all()
    return render(request, "concesionario/leerAutos.html", {"autos":totalautos})

def eliminarCliente(request,id):
    clientes=cliente.objects.get(id=id)
    clientes.delete()
    totalclientes=auto.objects.all()
    return render(request, "concesionario/leerClientes.html", {"clientes":totalclientes})

def eliminarSucursal(request,id):
    sucursales=sucursal.objects.get(id=id)
    sucursales.delete()
    totalsucursales=sucursal.objects.all()
    return render(request, "concesionario/leerSucursales.html", {"sucursales":totalsucursales})
        




#view para formulario a mano:
#def clienteFormulario(request):
#    if request.method=="POST":
#        nombre=request.POST.get("nombre")
#        apellido=request.POST.get("apellido")
#        dni=request.POST.get("dni")
#        fecha_compra=request.POST.get("fecha_compra")
#        cliente1=cliente(nombre=nombre,apellido=apellido,dni=dni,fecha_compra=fecha_compra)
#        cliente1.save()
#        return render(request,"concesionarios/template1.html")
#    return render (request,"concesionarios/clienteFormulario.html")

