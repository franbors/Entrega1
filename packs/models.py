from django.db import models

class Paquete(models.Model):
    destino = models.CharField(max_length=40)    
    descripcion = models.CharField(max_length=200)   
    dias = models.IntegerField()
    fecha_partida = models.DateField()
    fecha_regreso = models.DateField()
    precio_publico = models.FloatField()
    costo = models.FloatField()
    oferta = models.BooleanField()
    activo = models.BooleanField()

class Meta:
        verbose_name = 'paquete'
        verbose_name_plural = 'paquetes'