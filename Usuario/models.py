from django.db import models

# Create your models here.

class Colaborador(models.Model):
    nombre = models.CharField(max_length=20)
    Edad = models.IntegerField()
    telefono = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to ="user",null=True)
    tiempo = models.IntegerField()
 
    def __str__(self):
        return self.nombre