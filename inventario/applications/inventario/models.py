from django.db import models
from applications.dispositivo.models import Marca, Modelo, Color
from applications.resguardante.models import Resguardante

# Create your models here.
class Inventario(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=150)
    marca = models.ForeignKey(
        Marca,
        on_delete=models.CASCADE,
    )
    modelo = models.ForeignKey(
        Modelo,
        on_delete=models.CASCADE,
    )
    no_serie = models.CharField(verbose_name="# serie", max_length=25, unique=True)
    color = models.ForeignKey(
        Color, 
        on_delete=models.CASCADE,
    )
    estado_fisico = models.CharField(verbose_name="Estado físico", max_length=150)
    num_factura = models.CharField(verbose_name="# factura", max_length=30)
    nombre_resguardante = models.ForeignKey(
        Resguardante,
        on_delete=models.CASCADE
    )
    observaciones = models.TextField(verbose_name="Observaciones / Comentarios", blank=True)
    created = models.DateField(verbose_name="Creado", auto_now=True)


    class Meta:
        verbose_name = "Inventario"
        verbose_name_plural = "Inventarios"
        db_table = "inventario"

    def __str__(self):
        return self.no_serie
