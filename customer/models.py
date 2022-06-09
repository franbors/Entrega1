from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    pasaporte = models.IntegerField()
    vencimiento = models.DateField()
    dni = models.IntegerField()
    domicilio = models.CharField(max_length=40)
    telefono = models.IntegerField()