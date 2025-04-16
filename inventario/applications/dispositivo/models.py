from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(verbose_name="Nombre marca", max_length=50, unique=True)
    created = models.DateField(verbose_name="Creado", auto_now=True)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        db_table = "marca"

    def __str__(self):
        return self.nombre
    

class Modelo(models.Model):
    nombre = models.CharField(verbose_name="Nombre modelo", max_length=80, unique=True)
    created = models.DateField(verbose_name="Creado", auto_now=True)

    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"
        db_table = "modelo"

    def __str__(self):
        return self.nombre
    

class Color(models.Model):
    nombre = models.CharField(verbose_name="Color", max_length=80, unique=True)
    created = models.DateField(verbose_name="Creado", auto_now=True)

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colores"
        db_table = "color"

    def __str__(self):
        return self.nombre
    

class Factura(models.Model):
    no_factura = models.CharField(verbose_name="# factura", max_length=80, unique=True)
    proveedor = models.CharField(verbose_name="Proveedor", max_length=100, unique=True)
    fecha_emision = models.DateField(verbose_name="Fecha emisión")
    created = models.DateField(verbose_name="Creado", auto_now=True)

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
        db_table = "factura"

    def __str__(self):
        return self.no_factura


