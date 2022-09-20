
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from datetime import datetime

class auto(models.Model):
    marca=models.CharField(max_length=50)
    patente=models.CharField(max_length=50)
    modelo=models.IntegerField()
    fecha_ing=models.DateField()
    
    def __str__(self):
        return self.patente

class post(models.Model):
    
    usuario=models.ForeignKey(User,related_name="usuario",on_delete=models.CASCADE)
    titulo_del_post=models.CharField(max_length=100)
    subtitulo=models.CharField(max_length=50)
    posteo=RichTextField(blank=True,null=True)
    fecha=models.DateTimeField(default=datetime.now)
    imagen=models.ImageField(upload_to="posteos",blank=True,null=True)

    def __str__(self):
        return self.titulo_del_post

class cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni=models.IntegerField()
    fecha_compra=models.DateField()
    
    def __str__(self):
        return self.dni