from django.contrib import admin

from .models import Alumno


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ("legajo", "usuario", "carrera", "fecha_ingreso")
    list_filter = ("carrera",)
    search_fields = ("legajo", "usuario__username", "usuario__email")

# Register your models here.
