from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    dni = models.CharField(max_length=20, unique=True, blank=True, null=True)
    es_alumno = models.BooleanField(default=False)
    es_profesor = models.BooleanField(default=False)

    def __str__(self):
        return self.get_full_name() or self.username
