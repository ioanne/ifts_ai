from django.contrib import admin

from .models import Carrera


@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre")
    search_fields = ("codigo", "nombre")

# Register your models here.
