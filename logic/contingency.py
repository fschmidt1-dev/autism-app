"""
contingency.py — Generación del Plan B a partir de una ruta seleccionada.
Funciones puras que transforman datos crudos en estructuras de presentación.
Sin I/O, sin Streamlit, sin side effects.
"""

from logic.router import clasificar_afluencia, clasificar_ruido, seleccionar_ruta_optima
from data.routes import obtener_rutas_viables
from logic.validator import validar_lista_rutas


def generar_plan_b() -> dict:
    """
    Ejecuta el pipeline completo: obtiene rutas viables → selecciona óptima → formatea Plan B.
    Outputs: dict con claves: incidencia, pasos, afluencia_label, ruido_label, retraso_label.
    Errors: propaga ErrorValidacion si no hay rutas viables disponibles.
    """
    rutas_viables = obtener_rutas_viables()
    validar_lista_rutas(rutas_viables)

    ruta = seleccionar_ruta_optima(rutas_viables)

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
        "retraso_label": f"+{ruta['retraso_minutos']} minutos"
    }
