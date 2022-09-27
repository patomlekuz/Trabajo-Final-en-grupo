from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField,RichTextFormField
from datetime import datetime

from concesionarios.models import post

class ClienteFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    dni=forms.IntegerField()
    fecha_compra=forms.DateField(input_formats=['%Y-%m-%d'])

class AutoFormulario(forms.Form):
    marca=forms.CharField(max_length=50)
    patente=forms.CharField(max_length=50)
    modelo=forms.IntegerField()
    fecha_ing=forms.DateField(input_formats=['%Y-%m-%d'])

class PostFormulario(forms.ModelForm):
    
    titulo_del_post=forms.CharField(max_length=100)
    subtitulo=forms.CharField(max_length=50)
    fecha=forms.DateTimeField(initial=datetime.now())
    imagen=forms.ImageField()
    class Meta:
        model=post
        fields=("posteo",)


class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model= User
        fields= ["username","email","password1","password2"]
        help_texts= {k:"" for k in fields}