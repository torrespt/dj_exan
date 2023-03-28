from django.db import models

# Create your models here.
class Autos(models.Model):
    marca=models.TextField(max_length=20)
    nombre=models.TextField(max_length=30)
    modelo=models.IntegerField()
    color=models.TextField(max_length=20)

class Clientes(models.Model):
    nombre=models.TextField(max_length=20)
    apellido=models.TextField(max_length=30)
    direccion=models.TextField(max_length=200)
    email=models.TextField(max_length=250)
    telefono=models.TextField(max_length=20)