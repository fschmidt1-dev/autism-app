"""
config.py — Única fuente de verdad para todas las constantes del sistema.
Ningún otro archivo usa números mágicos o strings literales de configuración.
"""

# --- IDENTIDAD DEL PRODUCTO ---
APP_TITLE = "Ruteo Táctico"
APP_SUBTITLE = "SISTEMA DE RUTEO TÁCTICO"
APP_ICON = "⬛"

# --- COLORES DEL SISTEMA (DESIGN TOKENS) ---
COLOR_NAVY = "#1E2761"
COLOR_CORAL = "#F96167"
COLOR_GOLD = "#F9E795"
COLOR_CREAM = "#FAF7F2"
COLOR_TINTA = "#1A1A1A"
COLOR_MUTED = "#6B6B6B"
COLOR_BG = "#0E1117"
COLOR_SURFACE = "#1A1A1A"
COLOR_BORDER = "#333333"
COLOR_SUCCESS = "#2ECC71"

# --- UMBRALES SENSORIALES ---
AFLUENCIA_UMBRAL_ALTO = 70
AFLUENCIA_UMBRAL_MEDIO = 45
RUIDO_UMBRAL_ALTO_DB = 75
RUIDO_UMBRAL_MEDIO_DB = 60

# --- TIEMPOS ---
SPINNER_DELAY_SEGUNDOS = 1.2

# --- TIPOS DE INCIDENCIA (demo) ---
TIPOS_INCIDENCIA = [
    "Avería mecánica",
    "Aglomeración extrema",
    "Interrupción total de servicio"
]

TIPO_INCIDENCIA_DEFAULT = "Avería mecánica"

# --- RUTAS DE DEMO ---
RUTAS_DISPONIBLES = ["L10 Norte → Chamartín", "L6 → Príncipe Pío", "L1 → Atocha"]
RUTA_DEMO_DEFAULT = "L10 Norte → Chamartín"
RUTA_DEMO_AFLUENCIA_PCT = 65
RUTA_DEMO_RUIDO_DB = 68

# --- SENSORY CHECK DIARIO ---
CONDICION_SENSORIAL_HOY = "Moderada"   # En producción: dato real de APIs de tráfico
CONDICION_SENSORIAL_DETALLE = "Hora punta activa. Vagones al 65%. Recomendado: auriculares."

# --- SILENT CARD ---
SILENT_CARD_DESTINO = "Chamartín"
SILENT_CARD_TEXTO = "Por favor, lléveme a la estación de Chamartín.\nRuta silenciosa si es posible.\nGracias."

# --- LABELS DE UI / MICROCOPY ---
LABEL_BOTON_INCIDENCIA = "INCIDENCIA DETECTADA · RECALCULAR RUTA"
LABEL_BOTON_RESET = "VIAJE COMPLETADO · VOLVER AL INICIO"
LABEL_BOTON_SILENT = "MODO SILENCIOSO · MOSTRAR AL CONDUCTOR"
LABEL_BOTON_VOLVER = "← VOLVER AL PLAN B"
LABEL_ESTADO_NOMINAL = "ESTADO: VIAJE EN CURSO"
LABEL_PLAN_B_ACTIVO = "PLAN B ACTIVO:"
LABEL_SPINNER_CALCULO = "Procesando anomalía. Calculando ruta de menor impacto sensorial..."
LABEL_TOAST_RESET = "Viaje cerrado. El sistema está listo para el próximo trayecto."
LABEL_ERROR_SIN_RUTAS = "No hay rutas viables disponibles para este tipo de incidencia. Prueba con otro tipo."
LABEL_EMPTY_SELECTOR = "Selecciona tu ruta activa para comenzar."
