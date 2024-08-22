from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=500)
    tiempo = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(9)
        ])
    costo = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    servicio = models.ForeignKey(
        'servicios.Servicio',
        on_delete=models.CASCADE,
        related_name='tareas')
    nombre = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=500)
    tiempo = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(9)
        ])
    costo = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)

    def __str__(self):
        if self.nombre == None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return f'{self.nombre} | {self.servicio}'


class Recurso(models.Model):
    servicio = models.ForeignKey(
        'servicios.Servicio',
        on_delete=models.CASCADE,
        related_name='recursos')
    puesto = models.CharField(max_length=30)
    costo = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.puesto} | {self.servicio}'
