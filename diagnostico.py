# diagnostico.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "reporte_app.settings")
django.setup()

from contador.parser import parsear_reporte, _detectar_modo, _quitar_acentos
from contador.sinonimos import normalizar_concepto

RUTA = r"C:\Users\Muni\Desktop\estadisticas.txt"

with open(RUTA, encoding="utf-8") as f:
    lineas = f.readlines()


print("=" * 70)
print("TODAS LAS LÍNEAS QUE CONTENGAN 'RECORRIDO' (o similar)")
print("=" * 70)

modo = "normal"
total_por_linea = 0

for i, linea in enumerate(lineas, 1):
    s = linea.strip()
    if not s:
        continue

    nuevo_modo = _detectar_modo(s)
    if nuevo_modo:
        modo = nuevo_modo
        print(f"\n[{modo.upper()}] {s}")
        continue

    # ¿Esta línea es de recorrido?
    s_lower = _quitar_acentos(s).lower()
    if "recorrido" in s_lower or "recorridos" in s_lower:
        # Intentar parsear cantidad
        import re
        m = re.search(r"(\d+)", s)
        cantidad = int(m.group(1)) if m else 0

        # Qué concepto canónico le asigna el parser
        canonico = normalizar_concepto(_quitar_acentos(s.split("(")[0].split("*")[0].strip()))

        print(f"  L{i:3d} [{modo:6s}] {s:50s} → cantidad={cantidad:3d}  canonico={canonico}")
        total_por_linea += cantidad

print()
print("=" * 70)
print(f"TOTAL de recorridos contados en este diagnóstico: {total_por_linea}")
print("=" * 70)

# Ahora el parser completo
print("\n\nRESULTADO DEL PARSER COMPLETO:")
print("=" * 70)

with open(RUTA, encoding="utf-8") as f:
    texto = f.read()

resultado = parsear_reporte(texto)

for k, v in sorted(resultado["totales"].items()):
    if "recorrido" in k:
        print(f"  {k}: {v}")

print("\nNO RECONOCIDOS:")
for l in resultado["no_reconocidos"]:
    print(f"  {l}")