from django.contrib import admin
from .models import Reporte


@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):
    list_display = ("id", "fecha_creacion")
    readonly_fields = ("texto_original", "resultado_json", "fecha_creacion")