# contador/orden_oficial.py

# Estructura:
# Cada entrada es una tupla:
#   ("titulo_subtotal", [lista de claves], mostrar_siempre)
# Si titulo_subtotal es None, solo se muestran los items sin subtotal.

GRUPOS = [
    # ============ 1. TIPOS DE HECHOS VIALES ============
    ("Tipos de Hechos Viales", [
        ("volcamiento", True),
        ("colision vehicular", True),
        ("choque con objeto fijo", True),
        ("derrape vehicular", True),
        ("derrape de moto", True),
        ("encunetamiento", True),
        ("desbarrancamiento", True),
        ("atropellamiento", True),
        ("arrollamiento", True),
        ("experimentos de carga", True),
    ]),

    # ============ 2. ELIMINACION DE PELIGROS EN LA VIALIDAD ============
    ("Eliminación de Peligros en la Vialidad", [
        ("punto blanco", True),
        ("banda de rodamiento", True),
        ("chatarra o material ferroso", True),
        ("neumatico", True),
        ("mitigacion de riesgo vial", True),
        ("mantenimiento de las senalizaciones", True),
        ("tala y poda de arboles", True),
        ("desmontaje de poste caido", True),
        ("animal en descomposicion", True),
        ("bacheo emergente", True),
        ("rocas", True),
        ("retiro de defensa", True),
        ("deslizamiento", True),
        ("desmalezado", True),
        ("despeje de vias", True),
        ("eliminacion de insectos voladores y ponzonosos", True),
    ]),

    # ============ 3. RECORRIDOS ============
    ("recorridos", [
        ("recorrido vehicular", True),
        ("recorrido motorizado", True),
        ("recorrido punto a pie", True),
    ]),

    # ============ 4. SIN SUBTOTAL ============
    (None, [
        ("supervision de dispositivos viales en las cuadrillas", True),
        ("supervision de alumbrado publico", True),
        ("apoyo institucional", True),
        ("apoyo inter-institucional", True),
    ]),

    # ============ 5. APOYOS EN LA VIALIDAD ============
    ("Apoyos en la Vialidad", [
        ("auxilio vial", True),
        ("apoyo en atencion prehospitalaria", True),
        ("orientacion al usuario", True),
    ]),

    # ============ 6. DISPOSITIVOS DE PREVENCION ============
    ("Dispositivos de Prevención", [
        ("dispositivo de seguridad", True),
        ("cierre de vias", True),
        ("dispositivo de control de altura", True),
    ]),

    # ============ 7. SIN SUBTOTAL ============
    (None, [
        ("punto de observacion", True),
        ("beneficiados en la vialidad", True),
    ]),

    # ============ 8. MANTENIMIENTO Y RECARGAS DE TANQUES ============
    ("Mantenimiento y Recargas de Tanques", [
        ("recarga de tanques institucionales", True),
        ("mantenimiento de tanques de auxilio vial", True),
        ("recarga de tanques inter-institucionales", True),
        ("recarga de tanques de auxilio vial", True),
        ("trasegado", True),
    ]),

    # ============ 9. ATENCIONES PRE-HOSPITALARIAS ============
    ("Total Atenciones Pre-Hospitalarias", [
        ("ambulancias - atencion pre-hospitalaria", True),
        ("ambulancias - estabilizacion en el sitio", True),
        ("ambulancias - cuantificacion de signos vitales", True),
        ("ambulancias - cura local", True),
        ("ambulancias - atencion a lesionado en hecho vial", True),
        ("ambulancias - administracion de medicamentos bajo supervision medica", True),
        ("ambulancias - beneficiados pre-hospitalario", False),   # NO suma
    ]),

    # ============ 10. TRASLADOS AMBULANCIA ============
    ("Traslado de Ambulancias", [
        ("ambulancias - traslado emergente", True),
        ("ambulancias - traslado no emergente", True),
        ("ambulancias - traslado institucional", True),
        ("ambulancias - traslado fuera del estado", True),
        ("ambulancias - traslados", True),
        ("ambulancias - beneficiados de traslado en ambulancia", False),  # NO suma
    ]),

    # ============ 11. GRUA ============
    ("Grúa", [
        ("grua - servicio punto seguro", True),
        ("grua - traslado fuera del estado", True),
    ]),
]


# Nombres "bonitos" para mostrar
NOMBRES_BONITOS = {
    "incendio de vegetacion": "Incendio de Vegetación",
    "incendio de basura": "Incendio de Basura",
    "incendio de vehiculo": "Incendio de Vehículo",
    "volcamiento": "Volcamiento",
    "colision vehicular": "Colisión Vehicular",
    "choque con objeto fijo": "Choque con Objeto Fijo",
    "derrape vehicular": "Derrape Vehicular",
    "derrape de moto": "Derrape de Moto",
    "encunetamiento": "Encunetamiento",
    "desbarrancamiento": "Desbarrancamiento",
    "atropellamiento": "Atropellamiento",
    "arrollamiento": "Arrollamiento",
    "experimentos de carga": "Experimentos de Carga",
    "eventos adversos": "Eventos Adversos",
    "punto blanco": "Punto Blanco",
    "banda de rodamiento": "Banda de Rodamiento",
    "chatarra o material ferroso": "Chatarra o Material Ferroso",
    "neumatico": "Neumático",
    "mitigacion de riesgo vial": "Mitigación de Riesgo Vial",
    "mantenimiento de las senalizaciones": "Mantenimiento de las Señalizaciones",
    "tala y poda de arboles": "Tala y Poda de Árboles",
    "desmontaje de poste caido": "Desmontaje de Poste Caído",
    "animal en descomposicion": "Animal en Descomposición",
    "bacheo emergente": "Bacheo Emergente",
    "rocas": "Rocas",
    "retiro de defensa": "Retiro de Defensa",
    "deslizamiento": "Deslizamiento",
    "desmalezado": "Desmalezado",
    "despeje de vias": "Despeje de Vías",
    "eliminacion de insectos voladores y ponzonosos": "Eliminación de Insectos Voladores y Ponzoñosos",
    "recorrido vehicular": "Recorridos Vehicular",
    "recorrido motorizado": "Recorridos Motorizado",
    "recorrido punto a pie": "Recorridos Punto a Pie",
    "supervision de dispositivos viales en las cuadrillas": "Supervisión de Dispositivos Viales en las Cuadrillas",
    "supervision de alumbrado publico": "Supervisión de Alumbrado Público",
    "apoyo institucional": "Apoyo Institucional",
    "apoyo inter-institucional": "Apoyo Inter-Institucional",
    "inspeccion de riesgo vial": "Inspección de Riesgo Vial",
    "inspeccion de tanques de auxilio vial": "Inspección de Tanques de Auxilio Vial",
    "auxilio vial": "Auxilio Vial",
    "carabobenos": "Carabobeños",
    "visitante": "Visitante",
    "remolque tipo enganche": "Remolque Tipo Enganche",
    "apoyo en atencion prehospitalaria": "Apoyo en Atención Prehospitalaria",
    "rescate de lesionados": "Rescate de Lesionados",
    "apoyo en recuperacion y traslado de cadaveres": "Apoyo en Recuperación y Traslado de Cadáveres",
    "orientacion al usuario": "Orientación al Usuario",
    "dispositivo de seguridad": "Dispositivo de Seguridad",
    "dispositivo de regulacion y control de velocidad en autopista": "Dispositivo de Regulación y Control de Velocidad en Autopista (Recova)",
    "cierre de vias": "Cierre de Vías",
    "dispositivo de control de altura": "Dispositivo de Control de Altura",
    "habilitacion de canal de contra flujo": "Habilitación de Canal de Contra Flujo",
    "punto de observacion": "Punto de Observación",
    "beneficiados en la vialidad": "Beneficiados en la Vialidad",
    "resarcimiento de danos": "Resarcimiento de Daños",
    "riego de areas verdes": "Riego de Áreas Verdes",
    "mantenimiento de tanques de auxilio vial": "Mantenimiento de Tanques de Auxilio Vial",
    "recarga de tanques institucionales": "Recarga de Tanques Institucionales",
    "recarga de tanques inter-institucionales": "Recarga de Tanques Inter-Institucionales",
    "recarga de tanques de auxilio vial": "Recarga de Tanques de Auxilio Vial",
    "trasegado": "Trasegado",
    "desinfeccion institucional": "Desinfección Institucional",
    "desinfeccion inter-institucional": "Desinfección Inter-Institucional",
    "desinfeccion comunitaria": "Desinfección Comunitaria",
    "ambulancias - atencion pre-hospitalaria": "Atención Pre-Hospitalaria",
    "ambulancias - administracion de medicamentos bajo supervision medica": "Administración de Medicamentos Bajo Supervisión Médica",
    "ambulancias - estabilizacion en el sitio": "Estabilización en el Sitio",
    "ambulancias - cuantificacion de signos vitales": "Cuantificación de Signos Vitales",
    "ambulancias - cura local": "Cura Local",
    "ambulancias - atencion a lesionado en hecho vial": "Atención a Lesionado en Hecho Vial",
    "ambulancias - beneficiados pre-hospitalario": "Beneficiados Pre-Hospitalario",
    "ambulancias - traslado emergente": "Traslado Emergente",
    "ambulancias - traslado no emergente": "Traslado No Emergente",
    "ambulancias - traslado institucional": "Traslado Institucional",
    "ambulancias - traslado fuera del estado": "Traslado Fuera del Estado",
    "ambulancias - traslados": "Traslados",
    "ambulancias - beneficiados de traslado en ambulancia": "Beneficiados de Traslado en Ambulancia",
    "grua - servicio punto seguro": "Servicio Punto Seguro",
    "grua - traslado fuera del estado": "Traslado Fuera del Estado",
}


def construir_reporte(totales: dict) -> list:
    """
    Devuelve una lista de bloques con:
      - titulo: nombre del grupo (puede ser None)
      - items: [(nombre_bonito, valor), ...] solo con valor > 0
      - subtotal: suma de items que tienen suma_al_subtotal=True
    """
    bloques_resultado = []

    for titulo, claves in GRUPOS:
        items = []
        subtotal = 0
        for clave, suma in claves:
            valor = totales.get(clave, 0)
            if valor > 0:
                nombre = NOMBRES_BONITOS.get(clave, clave)
                items.append((nombre, valor))
                if suma:
                    subtotal += valor

        if items:
            bloques_resultado.append({
                "titulo": titulo,
                "items": items,
                "subtotal": subtotal,
            })

    return bloques_resultado





