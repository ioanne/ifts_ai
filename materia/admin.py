from django.contrib import admin

from .models import Materia


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre", "carrera", "carga_horaria")
    list_filter = ("carrera",)
    search_fields = ("codigo", "nombre")

# Register your models here.
