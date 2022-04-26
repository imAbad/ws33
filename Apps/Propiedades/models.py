from django.db import models
from Apps.Propiedades.choices import propiedades, operaciones, moneda
from django.utils.timezone import datetime

class Properties (models.Model, models.DecimalField):
    nombre = models.CharField(max_length=50)
    
    slug = models.SlugField(max_length = 250)
    
    
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=50)
    costo = models.DecimalField(max_digits=15, decimal_places=2)
    moneda = models.CharField(
        max_length=10, choices=moneda, default='')
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    estacionamientos = models.IntegerField()
    terreno = models.DecimalField(max_digits=10, decimal_places=2)
    construccion = models.DecimalField(max_digits=10, decimal_places=2)
    pisos = models.IntegerField()
    operacion = models.CharField(
        max_length=10, choices=operaciones, default='')
    propiedad = models.CharField(
        max_length=20, choices=propiedades, default='')
    
   
    
   

    def __str__(self):
        return self.nombre


class imagenPropiedades(models.Model):
    imagen = models.ImageField(upload_to='propiedades')
    propiedad = models.ForeignKey(
    Properties, on_delete=models.CASCADE, related_name="imagenes")
    
    def __str__(self):
        return self.propiedad.nombre
    
