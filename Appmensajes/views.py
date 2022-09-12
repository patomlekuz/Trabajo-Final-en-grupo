from django.shortcuts import render
from Appmensajes.models import Mensaje
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic.list import ListView
from django.contrib.auth.models import User
@login_required
def mensajeFormulario(request):
    if request.method=="POST":
        form=ContenidoMensaje(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            autor=request.POST.get("username",None)
            receptor=info.get("receptor")
            if User.objects.filter(username=receptor).exists():
                receptor=User.objects.get(username=receptor)
                return render(request,"concesionario/mensajeFormulario.html",{"mensaje":"no existe nadie con ese usuario"})
            titulo=info.get("titulo")
            mensaje=info.get("mensaje")       
            usuario=Mensaje.objects.get(autor=autor)
            msj=Mensaje(autor=usuario,titulo=titulo,mensaje=mensaje)
            msj.save()
            return render(request,"concesionario/mensajeFormulario.html",{"mensaje":"mensaje enviado"})
        else:
            return render(request,"concesionario/mensajeFormulario.html",{"miformulario":form,"mensaje":"No lleno todos los campos"})
    else:
        form=ContenidoMensaje()
        return render(request,"concesionario/mensajeFormulario.html",{"miformulario":form})
    
"""def sucursalFormulario(request):
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
        return render(request,"concesionario/sucursalFormulario.html",{"formulario":miFormularios})"""