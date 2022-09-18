from django.http import HttpResponse
from django.shortcuts import render
from .models import auto,post,cliente
from django.template import Context,Template,loader
from concesionarios.forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

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

def postFormulario(request):
    if request.method=="POST":
        miFormulariop = PostFormulario(request.POST)
        print(miFormulariop)
        if miFormulariop.is_valid():
            info=miFormulariop.cleaned_data
            print(info)
            usuario=info.get("usuario")
            titulo_del_post=info.get("titulo_del_post")
            auto=info.get("auto")
            #imagen=info.get("imagen")
            posteo=info.get("posteo")
            post1=post(usuario=usuario,titulo_del_post=titulo_del_post,auto=auto,posteo=posteo)#,imagen=imagen)
            post1.save()
            return render(request,"concesionario/template1.html",{"mensaje":"Buen posteo"})
        else:
            return render(request,"concesionario/template1.html",{"mensaje":"Ese posteo no se generó"})
    else:
        miFormulariop=PostFormulario()
        return render(request,"concesionario/postFormulario.html",{"formulario":miFormulariop})

@login_required
def buscar_post(request):
    if request.GET.get("titulo_del_post"):
        titulo=request.GET["titulo_del_post"]
        posts=post.objects.filter(titulo_del_post=titulo)
        if len(posts)!=0:
            return render (request, "concesionario/resultadosBusquedaPost.html",{"posts":posts})
        else:
            return render (request, "concesionario/resultadosBusquedaPost.html",{"mensaje": "no hay un post con ese título"})
    else:
        return render (request, "concesionario/busquedaPost.html",{"mensaje": "No ingresaste ningun dato"})

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

def busquedaPost(request):
    return render(request,"concesionario/busquedaPost.html")

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

def leerPosts(request):
    posts=post.objects.all()
    return render(request, "concesionario/leerPosts.html", {"posts":posts})

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

def eliminarPost(request,id):
    posts=post.objects.get(id=id)
    posts.delete()
    totalposts=post.objects.all()
    return render(request, "concesionario/leerPosts.html", {"posts":totalposts})
        
def login_request(request):
    if request.method=="POST":
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario=request.POST["username"]
            clave=request.POST["password"]
            acceso=authenticate(username=usuario,password=clave)
            if acceso is not None:
                login(request, acceso)
                return render(request,"concesionario/template1.html",{"mensaje":f"Sesion iniciada correctamente,Bienvenido {usuario}"}) 
            else:
                return render(request,"concesionario/login.html",{"form":form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request,"concesionario/login.html",{"form":form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request,"concesionario/login.html",{"form":form})

def register(request):
    if request.method=="POST":
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            return render(request,"concesionario/template1.html",{"mensaje":f"Usuario {username} creado exitosamente"})
    else:
        form=UserRegisterForm()
    return render(request,"concesionario/register.html",{"form":form})