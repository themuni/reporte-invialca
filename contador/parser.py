# contador/parser.py
import re
import unicodedata
from collections import defaultdict
from .sinonimos import (
    normalizar_concepto,
    normalizar_concepto_metro,
    normalizar_concepto_grua,
    CONCEPTOS_IGNORADOS,
)


def _quitar_acentos(texto: str) -> str:
    """'Orientación' -> 'Orientacion'. También ñ -> n."""
    if not texto:
        return ""
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return texto.replace("ñ", "n").replace("Ñ", "N")

# Detecta: concepto (03) | concepto 01 | concepto *1 | concepto (11 | concepto .01
RE_CONCEPTO = re.compile(
    r'^\s*[-•\*]?\s*'
    r'(?P<concepto>[A-Za-zÁÉÍÓÚÑÜáéíóúñü][A-Za-zÁÉÍÓÚÑÜáéíóúñü\s\.\-]+?)'
    r'\s*[\(\*]?\s*'
    r'(?P<cantidad>\d{1,4})'
    r'\s*\)?\s*$'
)

VARIANTES_APOYO_INVIALCA = {
    "apoyo a personal de invialca",
    "apoyo personal de invialca",
    "apoyo a personal invialca",
    "apoyo al personal de invialca",
    "apoyo institucional invialca",
    "apoyo al personal invialca",
    "apoyo institucional",
    "apoyos institucionales",
}

VARIANTES_TRASLADO_INSTITUCIONAL = {
    "traslado institucional",
    "traslados institucionales",
    "traslado institucional (02)",  # por si acaso
}

def _detectar_modo(linea: str) -> str | None:
    """
    Devuelve 'metro', 'grua', 'normal' o None (si no es encabezado de unidad).
    """
    limpia = _quitar_acentos(linea).lower()
    limpia = limpia.replace("*", " ").replace("•", " ")
    limpia = " ".join(limpia.split())

    if "unidad" in limpia:
        if "unidad metro" in limpia:
            return "metro"
        if "unidad grua" in limpia:
            return "grua"
        return "normal"

    if limpia.startswith("pac ") or limpia.startswith("pac-") or limpia == "pac":
        return "normal"

    return None

def parsear_reporte(texto: str) -> dict:
    """
    Lógica:
      - Si modo == 'metro' y el concepto pertenece al bloque 14 → bucket ambulancias.
      - Si modo == 'grua'  y el concepto pertenece al bloque 15 → bucket grua.
      - En cualquier otro caso → sinónimos normales (bloques 1-13).
      - Apoyo a personal de invialca cuenta SIEMPRE → apoyo institucional.
    """
    totales = defaultdict(int)
    no_reconocidos = []
    modo = "normal"

    for linea in texto.splitlines():
        linea_strip = linea.strip()
        if not linea_strip:
            continue

        # 1) ¿Encabezado de unidad?
        nuevo_modo = _detectar_modo(linea_strip)
        if nuevo_modo is not None:
            modo = nuevo_modo
            continue

        # 2) Ignorar líneas decorativas con asteriscos
        if linea_strip.startswith("*") and linea_strip.endswith("*") \
                and not re.search(r"\d", linea_strip):
            continue

        # 3) Intentar parsear concepto + cantidad
        m = RE_CONCEPTO.match(linea_strip)
        if not m:
            continue

        concepto_raw = _quitar_acentos(m.group("concepto").strip())
        cantidad = int(m.group("cantidad"))
        concepto_limpio = " ".join(concepto_raw.lower().split())

        if concepto_limpio in CONCEPTOS_IGNORADOS:
            continue

        # 4) Apoyo a personal de invialca → SIEMPRE apoyo institucional
        if concepto_limpio in VARIANTES_APOYO_INVIALCA:
            totales["apoyo institucional"] += cantidad
            continue
        

        # 5) Si estamos en METRO, probar primero bloque 14
        if modo == "metro":
            canonico_metro = normalizar_concepto_metro(concepto_raw)
            if canonico_metro:
                totales[canonico_metro] += cantidad
                continue
            # Si no es del bloque 14, cae al flujo normal (bloques 1-13)

        # 6) Si estamos en GRUA, probar primero bloque 15
        if modo == "grua":
            # Regla especial: traslado institucional bajo grua → apoyo institucional
            if concepto_limpio in VARIANTES_TRASLADO_INSTITUCIONAL:
                totales["apoyo institucional"] += cantidad
                continue

            canonico_grua = normalizar_concepto_grua(concepto_raw)
            if canonico_grua:
                totales[canonico_grua] += cantidad
                continue

        # 7) Flujo normal (bloques 1-13), sin importar el modo
        canonico = normalizar_concepto(concepto_raw)
        if canonico is None:
            no_reconocidos.append(linea_strip)
            continue

        totales[canonico] += cantidad

    return {
        "totales": dict(totales),
        "no_reconocidos": no_reconocidos,
    }
    
