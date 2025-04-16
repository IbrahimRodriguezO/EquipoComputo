from django.db import models

# Create your models here.
class Resguardante(models.Model):
    nombre = models.CharField(verbose_name="Nombre marca", max_length=50, unique=True)
    created = models.DateField(verbose_name="Creado", auto_now=True)

    class Meta:
        verbose_name = "Resguardante"
        verbose_name_plural = "Resguardantes"
        db_table = "resguardante"

    def __str__(self):
        return self.nombre
