from django.http import HttpResponse
from django.shortcuts import render
from .models import auto,post,Avatar
from django.template import Context,Template,loader
from concesionarios.forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 

def concesionario(request):
    #Esto viene a ser la landing
    return render (request,"concesionario/template1.html")

#view para formulario con django

def postFormulario(request):
    log=request.user
    if request.method=="POST":
        forms= PostFormulario(request.POST, request.FILES)
        
        if forms.is_valid():
            info=forms.cleaned_data
            usuario=log
            titulo_del_post=info["titulo_del_post"]
            subtitulo=info["subtitulo"]
            posteo=info["posteo"]
            fecha=info["fecha"]
            imagen=info["imagen"]
            post1=post(usuario=usuario,titulo_del_post=titulo_del_post,subtitulo=subtitulo,posteo=posteo,imagen=imagen,fecha=fecha)
            post1.save()
            return render(request,"concesionario/template1.html",{"mensaje":"Tu posteo se publico correctamente"})
        else:
            print(forms)
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

@login_required        
def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            print(info)
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.save()
            return render(request, 'concesionario/template1.html', {'mensaje':f"Perfil de {usuario} editado"})
    
    else:
        form= UserEditForm(instance=usuario)
    return render(request, 'concesionario/editarPerfil.html', {'form':form, 'usuario':usuario})



def agregarAvatar(request):
    if request.method == 'POST':
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if(len(avatarViejo)>0):
                avatarViejo.delete()
            avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'AppCoder/inicio.html', {'usuario':request.user, 'mensaje':'AVATAR AGREGADO EXITOSAMENTE', "imagen":obtenerAvatar(request)})
    else:
        formulario=AvatarForm()
    return render(request, 'AppCoder/agregarAvatar.html', {'form':formulario, 'usuario':request.user, "imagen":obtenerAvatar(request)})

#####funcion que trae la url del avatar###
def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen=""
    return imagen