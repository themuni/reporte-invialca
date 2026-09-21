import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .parser import parsear_reporte
from .orden_oficial import construir_reporte
from .models import Reporte


def index(request):
    return render(request, "contador/index.html")


@require_POST
def procesar(request):
    try:
        data = json.loads(request.body)
        texto = data.get("texto", "")
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido"}, status=400)

    if not texto.strip():
        return JsonResponse({"error": "El texto está vacío"}, status=400)

    resultado = parsear_reporte(texto)
    bloques = construir_reporte(resultado["totales"])

    reporte = Reporte.objects.create(
        texto_original=texto,
        resultado_json=resultado,
    )

    return JsonResponse({
        "ok": True,
        "reporte_id": reporte.pk,
        "bloques": bloques,
        "no_reconocidos": resultado["no_reconocidos"],
    })