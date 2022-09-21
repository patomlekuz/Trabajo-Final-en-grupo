from django.http import HttpResponse
from django.shortcuts import render
from .models import auto,post,cliente
from django.template import Context,Template,loader
from concesionarios.forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 

def concesionario(request):
    #Esto viene a ser la landing
    return render (request,"concesionario/template1.html")

#view para formulario con django

def postFormulario(request):
    log=request.user
    if request.method=="POST":
        forms= PostFormulario(request.POST)
        
        if forms.is_valid():
            info=forms.cleaned_data
            
            usuario=log
            titulo_del_post=info["titulo_del_post"]
            subtitulo=info["subtitulo"]
            posteo=info["posteo"]
            fecha=info["fecha"]
            imagen=info["imagen"]
            post1=post(usuario=usuario,titulo_del_post=titulo_del_post,subtitulo=subtitulo,posteo=posteo,fecha=fecha,imagen=imagen)
            post1.save()
            return render(request,"concesionario/template1.html",{"mensaje":"Tu posteo se publico correctamente"})
        else:
            return render(request,"concesionario/template1.html",{"forms":forms,"mensaje":"Ese posteo no se generó"})
    else:
        forms=PostFormulario()
        return render(request,"concesionario/postFormulario.html",{"forms":forms})

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

def buscar_postid(request,id):
    titulo=post.objects.get(id=id)
    posts=post.objects.filter(titulo_del_post=titulo)
#    print(posts)
#    if len(posts)!=0:
    return render (request, "concesionario/resultadosBusquedaPost.html",{"posts":posts})
#    else:
#        return render (request, "concesionario/resultadosBusquedaPost.html",{"mensaje": "no hay un post con ese título"})

def busquedaPost(request):
    return render(request, "concesionario/busquedaPost.html")

def busquedaCliente(request):
    return render(request,"concesionario/busquedaCliente.html")

def busquedaAuto(request):
    return render(request,"concesionario/busquedaAuto.html")

def aboutus(request):
    return render(request,"concesionario/aboutus.html")

def leerPosts(request):
    posts=post.objects.all()
    return render(request, "concesionario/leerPosts.html", {"posts":posts})

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

def profile(request, username=None):
    current_user= request.user 
    if username and username != current_user.username:
        user= User.objects.get(username=username)
        posts= user.post.all() 
    else:
        posts= user.post.all()
        user= current_user     
    return render(request, 'concesionario/profile.html', {'user':user, 'posts':post})