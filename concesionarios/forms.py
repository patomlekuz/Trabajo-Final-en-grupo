from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class SucursalFormulario(forms.Form):
    provincia=forms.CharField(max_length=50)
    localidad=forms.CharField(max_length=50)
    empleados=forms.IntegerField()
    fecha_inaugural=forms.DateField(input_formats=['%Y-%m-%d'])

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model= User
        fields= ["username","email","password1","password2"]
        help_texts= {k:"" for k in fields}