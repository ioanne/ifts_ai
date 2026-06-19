from django.conf import settings
from django.db import models


class Profesor(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="perfil_profesor",
    )
    legajo = models.CharField(max_length=20, unique=True)
    especialidad = models.CharField(max_length=120, blank=True)

    class Meta:
        ordering = ["legajo"]

    def __str__(self):
        return f"{self.legajo} - {self.usuario}"
