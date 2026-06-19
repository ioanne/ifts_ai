from django.db import models


class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    carrera = models.ForeignKey(
        "carrera.Carrera",
        on_delete=models.CASCADE,
        related_name="materias",
    )
    carga_horaria = models.PositiveIntegerField(default=0)
    profesores = models.ManyToManyField(
        "profesor.Profesor",
        blank=True,
        related_name="materias",
    )

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
