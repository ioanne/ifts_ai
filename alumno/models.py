from django.conf import settings
from django.db import models


class Alumno(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="perfil_alumno",
    )
    carrera = models.ForeignKey(
        "carrera.Carrera",
        on_delete=models.PROTECT,
        related_name="alumnos",
    )
    legajo = models.CharField(max_length=20, unique=True)
    fecha_ingreso = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["legajo"]

    def __str__(self):
        return f"{self.legajo} - {self.usuario}"
