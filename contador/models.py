from django.db import models


class Reporte(models.Model):
    texto_original = models.TextField()
    resultado_json = models.JSONField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reporte #{self.pk} - {self.fecha_creacion:%Y-%m-%d %H:%M}"