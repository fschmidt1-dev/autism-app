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

# --- UMBRALES SENSORIALES ---
AFLUENCIA_UMBRAL_ALTO = 70       # % de ocupación — sobre esto se marca como "Alta"
AFLUENCIA_UMBRAL_MEDIO = 45      # % de ocupación — sobre esto se marca como "Media"
RUIDO_UMBRAL_ALTO_DB = 75        # dB — sobre esto se marca como "Alto"
RUIDO_UMBRAL_MEDIO_DB = 60       # dB — sobre esto se marca como "Medio"

# --- TIEMPOS ---
SPINNER_DELAY_SEGUNDOS = 1.2     # Latencia simulada para procesamiento de anomalía

# --- ESTADO NOMINAL DE DEMOSTRACIÓN ---
RUTA_DEMO_NOMBRE = "L10 Norte"
RUTA_DEMO_DESTINO = "Chamartín"
RUTA_DEMO_AFLUENCIA_PCT = 65

# --- LABELS DE UI ---
LABEL_BOTON_INCIDENCIA = "INCIDENCIA DETECTADA · RECALCULAR"
LABEL_BOTON_RESET = "VIAJE COMPLETADO · RESETEAR"
LABEL_ESTADO_NOMINAL = "ESTADO: VIAJE EN CURSO"
LABEL_PLAN_B_ACTIVO = "PLAN B ACTIVO:"
LABEL_METRICAS = "MÉTRICAS DE ENTORNO:"
