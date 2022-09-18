from importlib.abc import PathEntryFinder
from django.db import models
from ckeditor.fields import RichTextField,RichTextFormField

# Create your models here.

class auto(models.Model):
    marca=models.CharField(max_length=50)
    patente=models.CharField(max_length=50)
    modelo=models.IntegerField()
    fecha_ing=models.DateField()
    
    def __str__(self):
        return self.patente

class post(models.Model):
    posteo=RichTextField(blank=True,null=True)
    usuario=models.CharField(max_length=50)
    titulo_del_post=models.CharField(max_length=100)
    auto=models.CharField(max_length=50)

#    imagen=models.ImageField()

    def __str__(self):
        return self.titulo_del_post

class cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni=models.IntegerField()
    fecha_compra=models.DateField()
    
    def __str__(self):
        return self.dni