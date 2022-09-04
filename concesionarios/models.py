from importlib.abc import PathEntryFinder
from django.db import models

# Create your models here.

class auto(models.Model):
    marca=models.CharField(max_length=50)
    patente=models.CharField(max_length=50)
    modelo=models.IntegerField()
    fecha_ing=models.DateField()
    
    def __str__(self):
        return self.patente

class sucursal(models.Model):
    provincia=models.CharField(max_length=50)
    localidad=models.CharField(max_length=50)
    empleados=models.IntegerField()
    fecha_inaugural=models.DateField()

    def __str__(self):
        return self.localidad

class cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni=models.IntegerField()
    fecha_compra=models.DateField()
    
    def __str__(self):
        return self.dni