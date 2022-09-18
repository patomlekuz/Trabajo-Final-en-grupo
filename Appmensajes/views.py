
from django.shortcuts import render,redirect
from .forms import ContenidoMensaje
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from .models import Mensaje
from django.contrib.auth.decorators import login_required
@login_required
def mensajeFormulario(request):
    usuario=request.user
    print(usuario)
    if request.method=="POST":
        forms=ContenidoMensaje(request.POST)
        if forms.is_valid():
            info=forms.cleaned_data
            
            receptor=info["receptor"]
            if User.objects.filter(username=receptor).exists():
                autor=usuario
                
                print(autor)
                titulo=info["titulo"]
                print(titulo)
                mensaje=info["mensaje"]
                print(mensaje)
                contenido=Mensaje(autor=autor,receptor=receptor,titulo=titulo,mensaje=mensaje)
                print(contenido)
                contenido.save()
                return render(request, "concesionario/mensajeFormulario.html",{"mensaje":"Mensaje Enviado"})
            else:
                
                return render(request, "concesionario/mensajeFormulario.html",{"forms":forms, "mensaje":"no existe un usuario con ese nombre"})
        else:
            return render(request, "concesionario/mensajeFormulario.html",{"forms":forms, "mensaje":"Mensaje o usuario invalidos"})
    else:
        forms=ContenidoMensaje()
        return render(request, "concesionario/mensajeFormulario.html",{"forms":forms, "mensaje":"Complete el formulario"})

def leerMensaje(request):
    receptor=request.user
    print(receptor)
    
    mensajes=Mensaje.objects.filter(receptor=receptor)
    if len(mensajes)!=0:
        cantmensajes=len(mensajes)
        return render(request,"concesionario/leerMensaje.html",{"mensajes":mensajes,"cantmensajes":cantmensajes})
    else:
        return render(request,"concesionario/leerMensaje.html",{"mensaje":"no tenes mensajes para leer"})

def eliminarMensajes(request,id):
    mensajes=Mensaje.objects.get(id=id)
    mensajes.delete()
    totalmensajes=Mensaje.objects.all()
    return render(request, "concesionario/leerMensaje.html",{"mensaje":"mensaje Eliminado","mensajes":totalmensajes})

def misMensajes(request,id):
    mensajes=Mensaje.objects.get(id=id)
    return render(request,"concesionario/misMensajes.html",{"mensajes":mensajes,"mensaje":"Mensaje Eliminado"})
"""def leerSucursales(request):
    sucursales=sucursal.objects.all()
    return render(request, "concesionario/leerSucursales.html", {"sucursales":sucursales})"""
"""def eliminarAuto(request,id):
    autos=auto.objects.get(id=id)
    autos.delete()
    totalautos=auto.objects.all()
    return render(request, "concesionario/leerAutos.html", {"autos":totalautos})"""
"""@login_required
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
    """

