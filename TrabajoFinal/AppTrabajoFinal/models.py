from django.db import models

class Persona(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()

class Perro(models.Model):
    nombre=models.CharField(max_length=50)
    raza=models.CharField(max_length=50)
    edad=models.IntegerField()

class Gato(models.Model):
    nombre=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    edad=models.IntegerField()
