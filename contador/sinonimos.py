# contador/sinonimos.py
"""
Diccionario de sinónimos para normalizar los conceptos del reporte.
CLAVE = nombre canónico oficial.
VALOR = lista de variantes escritas.
Todos los textos SIN acentos (el parser los quita antes).
"""

# ============================================================
# BLOQUES 1 a 13: CONCEPTOS DE UNIDADES NORMALES
# ============================================================
SINONIMOS = {

    # ============ 1. EVENTOS FORTUITOS ============
    "incendio de vegetacion": [
        "incendio de vegetacion", "incendio vegetacion",
        "incendio de maleza", "incendio forestal",
    ],
    "incendio de basura": [
        "incendio de basura", "incendio basura",
    ],
    "incendio de vehiculo": [
        "incendio de vehiculo", "incendio vehiculo",
        "incendio de carro",
    ],

    # ============ 2. TIPOS DE HECHOS VIALES ============
    "volcamiento": [
        "volcamiento", "volcadura", "volteo",
    ],
    "colision vehicular": [
    "colision vehicular", "colision", "colisiones",
    "colision por trayecto", "colision multiple",
    "colision por alcance", "colision frontal",
    "colision lateral",
    ],
    "choque con objeto fijo": [
        "choque con objeto fijo", "colision con objeto fijo",
        "choque objeto fijo", "choque"
    ],
    "derrape vehicular": [
        "derrape vehicular", "derrape", "derrapes",
        "derrape de vehiculo",
    ],
    "derrape de moto": [
        "derrape de moto", "derrape moto", "derrape de motocicleta",
        "derrapes de moto",
    ],
    "encunetamiento": [
        "encunetamiento", "encunetado", "encunetamientos",
    ],
    "desbarrancamiento": [
        "desbarrancamiento", "desbarrancado", "desbarrancamientos",
    ],
    "atropellamiento": [
        "atropellamiento", "atropello", "atropellamientos",
    ],
    "arrollamiento": [
        "arrollamiento", "arrollado", "arrollamientos",
    ],
    "experimentos de carga": [
        "experimentos de carga", "experimento de carga",
    ],

    # ============ 3. EVENTOS ADVERSOS ============
    "eventos adversos": [
        "eventos adversos", "evento adverso",
    ],

    # ============ 4. ELIMINACION DE PELIGROS EN LA VIALIDAD ============
    "punto blanco": [
        "punto blanco", "puntos blancos", "pb",
    ],
    "banda de rodamiento": [
        "banda de rodamiento", "bandas de rodamiento",
        "rodamiento", "rodamientos", "banda rodamiento",
    ],
    "chatarra o material ferroso": [
        "chatarra o material ferroso", "chatarra", "material ferroso",
        "chatarra material ferroso",
    ],
    "neumatico": [
        "neumatico", "neumaticos", "caucho", "cauchos",
    ],
    "mitigacion de riesgo vial": [
        "mitigacion de riesgo vial", "mitigacion riesgo vial",
        "mitigacion de riesgo", "mitigacion de riesgos",
    ],
    "mantenimiento de las senalizaciones": [
        "mantenimiento de las senalizaciones",
        "mantenimiento de senalizaciones",
        "mantenimiento senalizaciones",
        "senalizaciones",
    ],
    "tala y poda de arboles": [
        "tala y poda de arboles", "tala y poda", "poda de arboles",
        "tala de arboles",
    ],
    "desmontaje de poste caido": [
        "desmontaje de poste caido", "poste caido",
        "desmontaje poste caido",
    ],
    "animal en descomposicion": [
        "animal en descomposicion", "animal muerto",
    ],
    "bacheo emergente": [
        "bacheo emergente", "bacheo", "baches",
    ],
    "rocas": [
        "rocas", "roca",
    ],
    "retiro de defensa": [
        "retiro de defensa",
        "retiro de defensa lamina flex beam y new jersey",
        "retiro de lamina flex beam", "retiro new jersey",
    ],
    "deslizamiento": [
        "deslizamiento", "deslizamientos", "derrumbe",
    ],
    "desmalezado": [
        "desmalezado", "desmalezamiento",
    ],
    "despeje de vias": [
        "despeje de vias", "despeje de via", "despeje vias",
        "despeje de vial", "despeje vial",
    ],
    "eliminacion de insectos voladores y ponzonosos": [
        "eliminacion de insectos voladores y ponzonosos",
        "eliminacion de insectos", "insectos ponzonosos",
        "eliminacion de insectos voladores",
    ],

    # ============ 5. RECORRIDOS Y APOYOS INSTITUCIONALES ============
    "recorrido vehicular": [
        "recorrido vehicular", "recorridos vehiculares",
        "recorrido vehiculo", "recorrido preventivo",
        "recorridos preventivo", "recorridos preventivos",
    ],
    "recorrido motorizado": [
        "recorrido motorizado", "recorridos motorizados",
        "recorrido en moto",
    ],
    "recorrido punto a pie": [
        "recorrido punto a pie", "recorrido a pie",
        "recorrido punto pie", "recorrido pie",
    ],
    "supervision de dispositivos viales en las cuadrillas": [
        "supervicion de dispositivos viales en las cuadrillas",
        "supervision de dispositivos viales en las cuadrillas",
        "supervision de dispositivos viales",
        "supervicion de dispositivos viales",
    ],
    "supervision de alumbrado publico": [
        "supervicion de alumbrado publico",
        "supervision de alumbrado publico",
        "alumbrado publico",
    ],
    "apoyo institucional": [
        "apoyo institucional", "apoyos institucionales",
        "apoyo a personal de invialca",
        "apoyo personal de invialca",
        "apoyo a personal invialca",
        "apoyo al personal de invialca",
        "apoyo institucional invialca",
        "apoyo al personal invialca",
    ],
    "apoyo inter-institucional": [
        "apoyo inter-institucional", "apoyo interinstitucional",
        "apoyo inter institucional",
    ],
    "inspeccion de riesgo vial": [
        "inspeccion de riesgo vial", "inspeccion riesgo vial",
        "inspeccion de riesgo",
    ],
    "inspeccion de tanques de auxilio vial": [
        "inspeccion de tanques de auxilio vial",
        "inspeccion tanques de auxilio vial",
        "inspeccion de tanques",
    ],

    # ============ 6. APOYOS EN LA VIALIDAD ============
    "auxilio vial": [
        "auxilio vial", "auxilios viales",
    ],
    "carabobenos": [
        "carabobenos", "carabobeno", "carabobeños", "carabobeño",
    ],
    "visitante": [
        "visitante", "visitantes",
    ],
    "remolque tipo enganche": [
        "remolque tipo enganche", "remolque enganche",
        "remolque", "remolques",
    ],
    "apoyo en atencion prehospitalaria": [
        "apoyo en atencion prehospitalaria",
        "apoyo atencion prehospitalaria",
        "apoyo prehospitalario",
    ],
    "rescate de lesionados": [
        "rescate de lesionados", "rescate lesionados",
        "rescate de lesionado",
    ],
    "apoyo en recuperacion y traslado de cadaveres": [
        "apoyo en recuperacion y traslado de cadaveres",
        "traslado de cadaveres", "recuperacion de cadaveres",
        "apoyo recuperacion cadaveres",
    ],
    "orientacion al usuario": [
        "orientacion al usuario", "orientacion usuario",
        "orientacion al ciudadano", "orientacion ciudadano",
        "orientacion a usuarios", "orientacion a usuario",
        "orientacion", "orientaciones",
    ],

    # ============ 7. DISPOSITIVOS DE PREVENCION ============
    "dispositivo de seguridad": [
        "dispositivo de seguridad", "dispositivos de seguridad",
    ],
    "dispositivo de regulacion y control de velocidad en autopista": [
        "dispositivo de regulacion y control de velocidad en autopista",
        "dispositivo de regulacion y control de velocidad",
        "recova", "dispositivo recova",
    ],
    "cierre de vias": [
        "cierre de vias", "cierre de via", "cierre vias",
        "cierre parcial de vias", "cierre parcial de via",
        "cierre parcial vias", "cierre parcial vial",
    ],
    "dispositivo de control de altura": [
        "dispositivo de control de altura",
        "dispositivo decontrol de altura",
        "dispositivo control de altura",
        "control de altura",
    ],
    "habilitacion de canal de contra flujo": [
        "habilitacion de canal de contra flujo",
        "canal de contra flujo", "contra flujo",
    ],

    # ============ 8. PUNTOS DE OBSERVACION ============
    "punto de observacion": [
        "punto de observacion", "punto observacion",
        "punto atencion ciudadano", "punto atencion ciudadana",
        "punto de atencion ciudadano", "punto de atencion al ciudadano",
        "punto de atencion ciudadana", "punto atencion al ciudadano",
        "puntos de observacion",
        "puesto de atencion al ciudadano",
        "puesto de atencion ciudadano",
        "puesto atencion al ciudadano",
        "puesto de atencion ciudadana",
    ],

    # ============ 9. BENEFICIADOS ============
    "beneficiados en la vialidad": [
        "beneficiados en la vialidad", "beneficiados vialidad",
        "beneficiados", "beneficiarios",
        "personas beneficiadas", "persona beneficiada",
        "beneficiados en vialidad",
    ],

    # ============ 10. DAÑOS AL ESTADO ============
    "resarcimiento de danos": [
        "resarcimiento de danos", "resarcimiento",
        "danos al estado",
    ],

    # ============ 11. RIEGO DE AREAS VERDES ============
    "riego de areas verdes": [
        "riego de areas verdes", "regado de areas verdes",
        "riego areas verdes",
    ],

    # ============ 12. MANTENIMIENTO Y RECARGAS DE TANQUES ============
    "mantenimiento de tanques de auxilio vial": [
        "mantenimiento de tanques de auxilio vial",
        "mantenimiento de tanques", "mantenimiento tanques auxilio vial",
    ],
    "recarga de tanques institucionales": [
        "recarga de tanques institucionales",
        "recarga tanques institucionales",
        "recarga de tanques institucional",
        "recarga de tanque institucional",
    ],
    "recarga de tanques inter-institucionales": [
        "recarga de tanques inter-institucionales",
        "recarga de tanques interinstitucionales",
        "recarga tanques inter-institucionales",
    ],
    "recarga de tanques de auxilio vial": [
        "recarga de tanques de auxilio vial",
        "recarga tanques de auxilio vial",
        "recarga tanques auxilio vial",
    ],
    "trasegado": [
        "trasegado", "trasegados",
    ],

    # ============ 13. DESINFECCIONES ============
    "desinfeccion institucional": [
        "desinfeccion institucional", "desinfecciones institucionales",
    ],
    "desinfeccion inter-institucional": [
        "desinfeccion inter-institucional",
        "desinfeccion interinstitucional",
        "desinfecciones inter-institucionales",
    ],
    "desinfeccion comunitaria": [
        "desinfeccion comunitaria", "desinfecciones comunitarias",
    ],
}


# ============================================================
# BLOQUE 14: AMBULANCIAS (solo aparecen bajo *Unidad Metro*)
# ============================================================
SINONIMOS_METRO = {
    "ambulancias - atencion pre-hospitalaria": [
        "atencion pre-hospitalaria", "atencion prehospitalaria",
        "atencion pre hospitalaria",
    ],
    "ambulancias - administracion de medicamentos bajo supervision medica": [
        "administracion de medicamentos bajo supervision medica",
        "administracion de medicamentos",
        "medicamentos bajo supervision medica",
    ],
    "ambulancias - estabilizacion en el sitio": [
        "estabilizacion en el sitio",
        "estabilizado en el sitio",
        "estabilizacion en sitio",
    ],
    "ambulancias - cuantificacion de signos vitales": [
        "cuantificacion de signos vitales",
        "signos vitales",
    ],
    "ambulancias - cura local": [
        "cura local", "cura local",
    ],
    "ambulancias - atencion a lesionado en hecho vial": [
        "atencion a lesionado en hecho vial",
        "atencion de lesionado en hecho vial",
        "atencion a lesionados en hecho vial",
        "atencion de lesionados en hecho vial",
    ],
    "ambulancias - beneficiados pre-hospitalario": [
        "beneficiados pre-hospitalario",
        "beneficiados prehospitalario",
        "beneficiados pre hospitalario",
        "beneficiadas pre-hospitalario",
        "beneficiadas prehospitalario",
        "beneficiadas pre hospitalario",
        "beneficiados pre-hospitalaria",
        "beneficiados prehospitalaria",
        "beneficiadas pre-hospitalaria",
        "beneficiadas prehospitalaria",
    ],
    "ambulancias - traslado emergente": [
        "traslado emergente", "traslados emergentes",
    ],
    "ambulancias - traslado no emergente": [
        "traslado no emergente", "traslados no emergentes",
    ],
    "ambulancias - traslado institucional": [
        "traslado institucional", "traslados institucionales",
    ],
    "ambulancias - traslado fuera del estado": [
        "traslado fuera del estado", "traslados fuera del estado",
    ],
    "ambulancias - traslados": [
        "traslados", "traslado",
    ],
    "ambulancias - beneficiados de traslado en ambulancia": [
        "beneficiados de traslado en ambulancia",
        "beneficiados traslado en ambulancia",
        "beneficiadas de traslado en ambulancia",
        "beneficiadas traslado en ambulancia",
        "beneficiados ambulancia",
        "beneficiadas ambulancia",
        "beneficiados ambulacia",
        "beneficiadas ambulacia",
        "beneficiados en ambulancia",
        "beneficiadas en ambulancia",
        "beneficiadas de ambulancia",      
        "beneficiados de ambulancia",             
        "beneficiadas traslado de ambulancia",    
        "beneficiados traslado de ambulancia",    
        "beneficiadas de traslado de ambulancia", 
        "beneficiados de traslado de ambulancia", 
    ],
}


# ============================================================
# BLOQUE 15: GRUA (solo aparece bajo *Unidad Grúa*)
# ============================================================
SINONIMOS_GRUA = {
    "grua - servicio punto seguro": [
        "servicio punto seguro",
        "servicio a punto seguro",
        "servicio de punto seguro",
        "traslado a sitio seguro",
        "punto seguro",
    ],
    "grua - traslado fuera del estado": [
        "traslado fuera del estado",
        "traslados fuera del estado",
        "traslado foraneo",
    ],
}
VARIANTES_TRASLADO_INSTITUCIONAL = {
    "traslado institucional",
    "traslados institucionales",
}
# ============================================================
# CONCEPTOS QUE SE IGNORAN (rótulos/menbrete del reporte)
# ============================================================
CONCEPTOS_IGNORADOS = {
    "hecho vial",
    "hechos viales",
}

def normalizar_concepto(texto: str) -> str | None:
    """Devuelve el concepto canónico o None si no se reconoce."""
    if not texto:
        return None
    t = texto.lower().strip()
    t = " ".join(t.split())

    for canonico, variantes in SINONIMOS.items():
        if t in variantes:
            return canonico
    return None


def normalizar_concepto_metro(texto: str) -> str | None:
    """Igual que normalizar_concepto pero solo para conceptos de AMBULANCIAS."""
    if not texto:
        return None
    t = texto.lower().strip()
    t = " ".join(t.split())
    t = t.replace("pre-hospitalaria", "pre hospitalaria").replace(
        "pre-hospitalario", "pre hospitalario"
    )

    for canonico, variantes in SINONIMOS_METRO.items():
        variantes_limpias = [
            v.replace("pre-hospitalaria", "pre hospitalaria")
             .replace("pre-hospitalario", "pre hospitalario")
            for v in variantes
        ]
        if t in variantes_limpias:
            return canonico
    return None


def normalizar_concepto_grua(texto: str) -> str | None:
    """Igual que normalizar_concepto pero solo para conceptos de GRUA."""
    if not texto:
        return None
    t = texto.lower().strip()
    t = " ".join(t.split())

    for canonico, variantes in SINONIMOS_GRUA.items():
        if t in variantes:
            return canonico
    return None

