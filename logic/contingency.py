"""
contingency.py — Generación del Plan B a partir de tipo de incidencia.
Funciones puras. Sin I/O, sin Streamlit, sin side effects.
"""

from logic.router import seleccionar_ruta_optima, clasificar_afluencia, clasificar_ruido
from data.routes import obtener_rutas_por_tipo, obtener_rutas_viables
from logic.validator import validar_lista_rutas, ErrorValidacion
from config import TIPO_INCIDENCIA_DEFAULT


def generar_plan_b(tipo_incidencia: str = TIPO_INCIDENCIA_DEFAULT) -> dict:
    """
    Pipeline completo: filtra rutas por tipo → selecciona óptima → formatea Plan B.
    Inputs: tipo_incidencia — string del tipo de incidencia activo.
    Outputs: dict con claves: incidencia, pasos, afluencia_label, ruido_label, retraso_label.
    Errors: ErrorValidacion si no hay rutas viables para el tipo dado.
    """
    rutas = obtener_rutas_por_tipo(tipo_incidencia)

    if len(rutas) == 0:
        rutas = obtener_rutas_viables()

    validar_lista_rutas(rutas)
    ruta = seleccionar_ruta_optima(rutas)
    return formatear_plan_b(ruta)


def formatear_plan_b(ruta: dict) -> dict:
    """
    Convierte una ruta cruda en un dict listo para renderizar en UI.
    Inputs: ruta — dict de RutaContingencia con todos los campos.
    Outputs: dict con etiquetas legibles y pasos listos para iterar.
    """
    return {
        "incidencia": ruta["incidencia"],
        "pasos": ruta["pasos"],
        "afluencia_label": f"{ruta['afluencia_pct']}% ({clasificar_afluencia(ruta['afluencia_pct'])})",
        "ruido_label": f"{ruta['ruido_db']} dB ({clasificar_ruido(ruta['ruido_db'])})",
        "retraso_label": f"+{ruta['retraso_minutos']} minutos",
        "requiere_taxi": ruta["afluencia_pct"] == 0
    }
