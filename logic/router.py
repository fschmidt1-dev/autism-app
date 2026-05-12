"""
router.py — Selección de ruta óptima de contingencia según criterios sensoriales.
Todas las funciones son puras: mismo input → mismo output. Sin I/O, sin Streamlit.
"""

import random
from config import AFLUENCIA_UMBRAL_ALTO, AFLUENCIA_UMBRAL_MEDIO, RUIDO_UMBRAL_ALTO_DB, RUIDO_UMBRAL_MEDIO_DB
from logic.validator import validar_lista_rutas, validar_estructura_ruta


def clasificar_afluencia(afluencia_pct: int) -> str:
    """
    Convierte un porcentaje de afluencia a etiqueta legible.
    Inputs: afluencia_pct — entero 0-100.
    Outputs: string con clasificación ('Alta', 'Media', 'Baja').
    """
    if afluencia_pct >= AFLUENCIA_UMBRAL_ALTO:
        return "Alta"
    if afluencia_pct >= AFLUENCIA_UMBRAL_MEDIO:
        return "Media"
    return "Baja"


def clasificar_ruido(ruido_db: int) -> str:
    """
    Convierte dB a etiqueta legible de impacto sensorial.
    Inputs: ruido_db — entero en decibeles.
    Outputs: string con clasificación ('Alto', 'Medio', 'Bajo').
    """
    if ruido_db >= RUIDO_UMBRAL_ALTO_DB:
        return "Alto"
    if ruido_db >= RUIDO_UMBRAL_MEDIO_DB:
        return "Medio"
    return "Bajo"


def calcular_score_sensorial(ruta: dict) -> int:
    """
    Calcula un score de carga sensorial para una ruta (menor = mejor para Marc).
    Fórmula: afluencia + ruido_db. Determinista, sin pesos ocultos.
    Inputs: ruta — dict con 'afluencia_pct' y 'ruido_db'.
    Outputs: entero — score total de carga sensorial.
    """
    return ruta["afluencia_pct"] + ruta["ruido_db"]


def seleccionar_ruta_optima(rutas_viables: list) -> dict:
    """
    Selecciona la ruta con menor carga sensorial de una lista de rutas viables.
    En caso de empate, selecciona aleatoriamente entre las empatadas.
    Inputs: rutas_viables — lista de dicts de RutaContingencia, ya filtrada por viable==True.
    Outputs: dict con la ruta seleccionada.
    Errors: ValueError si la lista está vacía (validada antes de llamar).
    """
    validar_lista_rutas(rutas_viables)
    for ruta in rutas_viables:
        validar_estructura_ruta(ruta)

    score_minimo = min(calcular_score_sensorial(r) for r in rutas_viables)
    rutas_optimas = [r for r in rutas_viables if calcular_score_sensorial(r) == score_minimo]

    return random.choice(rutas_optimas)
