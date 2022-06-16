from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here.

class alimento(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    precio = models.IntegerField()
    descipcion = models.TextField
    tipo = models.BooleanField()
    peso = models.IntegerField()
    imagen = models.ImageField(upload_to ="alimentos",null=True)
    
    def __str__(self):
        return self.nombre
    
class juguete(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    precio = models.IntegerField()
    descipcion = models.TextField
    usado = models.BooleanField()
    cantidad = models.IntegerField()
    imagen = models.ImageField(upload_to ="juguetes",null=True)
    
    def __str__(self):
        return self.nombre
    
class agregar(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    precio = models.IntegerField()
    peso = models.IntegerField()
    imagen = models.ImageField(upload_to ="alimentos",null=True)
    
    
    def __str__(self):
        return self.nombre