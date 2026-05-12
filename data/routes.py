"""
routes.py — Repositorio in-memory de rutas de contingencia.
Única fuente de verdad para datos de rutas. No contiene lógica de selección.
Inputs: ninguno. Outputs: lista de dicts con estructura definida.
"""

from typing import TypedDict


class PasoContingencia(TypedDict):
    texto: str


class RutaContingencia(TypedDict):
    id: str
    incidencia: str
    pasos: list[str]
    afluencia_pct: int
    ruido_db: int
    retraso_minutos: int
    viable: bool


def obtener_rutas_contingencia() -> list[RutaContingencia]:
    """
    Devuelve todas las rutas de contingencia disponibles.
    Returns: lista de RutaContingencia con campos completos y tipados.
    """
    return [
        {
            "id": "contingencia_tribunal_40",
            "incidencia": "Avería mecánica en L10.",
            "pasos": [
                "Baja en la próxima estación (Tribunal).",
                "Usa la salida Norte (Calle Fuencarral).",
                "Toma el autobús 40 en la acera derecha."
            ],
            "afluencia_pct": 30,
            "ruido_db": 55,
            "retraso_minutos": 12,
            "viable": True
        },
        {
            "id": "contingencia_alonso_l5",
            "incidencia": "Corte de servicio por aglomeración en L10.",
            "pasos": [
                "No subas al tren. Retrocede a los tornos.",
                "Camina 400 metros al sur hacia Alonso Martínez.",
                "Sube a Línea 5, vagón de cola (menor afluencia)."
            ],
            "afluencia_pct": 45,
            "ruido_db": 62,
            "retraso_minutos": 18,
            "viable": True
        },
        {
            "id": "contingencia_taxi_silencioso",
            "incidencia": "Interrupción total de servicio en L10.",
            "pasos": [
                "Sal de la estación por cualquier salida.",
                "Abre esta pantalla y muéstrasela al conductor: 'Chamartín, por favor'.",
                "Sube sin hablar. El trayecto es 14 minutos."
            ],
            "afluencia_pct": 0,
            "ruido_db": 40,
            "retraso_minutos": 25,
            "viable": True
        }
    ]


def obtener_rutas_viables() -> list[RutaContingencia]:
    """
    Filtra y devuelve solo rutas marcadas como viables.
    Returns: lista de RutaContingencia donde viable == True.
    """
    todas = obtener_rutas_contingencia()
    return [ruta for ruta in todas if ruta["viable"] is True]
