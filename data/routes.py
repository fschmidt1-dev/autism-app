"""
routes.py — Repositorio in-memory de rutas de contingencia.
Única fuente de verdad para datos de rutas. Sin lógica de selección.
"""

from typing import TypedDict


class RutaContingencia(TypedDict):
    id: str
    tipo_incidencia: str
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
            "tipo_incidencia": "Avería mecánica",
            "incidencia": "Avería mecánica confirmada en L10. Servicio suspendido en tramo norte.",
            "pasos": [
                "Baja en la próxima estación (Tribunal). Usa la salida Norte.",
                "Camina 80 metros por Fuencarral hacia la derecha. Busca la marquesina azul.",
                "Sube al Bus 40. Vagón trasero — afluencia estimada 30%."
            ],
            "afluencia_pct": 30,
            "ruido_db": 55,
            "retraso_minutos": 12,
            "viable": True
        },
        {
            "id": "contingencia_alonso_l5",
            "tipo_incidencia": "Avería mecánica",
            "incidencia": "Avería mecánica en L10. Servicio interrumpido hasta nuevo aviso.",
            "pasos": [
                "No subas al tren. Retrocede a los tornos ahora.",
                "Camina 400 metros al sur. Destino: estación Alonso Martínez.",
                "Sube a Línea 5. Último vagón — menor densidad verificada."
            ],
            "afluencia_pct": 42,
            "ruido_db": 61,
            "retraso_minutos": 18,
            "viable": True
        },
        {
            "id": "contingencia_taxi_silencioso",
            "tipo_incidencia": "Interrupción total de servicio",
            "incidencia": "Corte total en L10. Sin alternativa en metro hasta reestablecimiento.",
            "pasos": [
                "Sal de la estación por cualquier salida. No esperes en el andén.",
                "Activa 'Modo Silencioso' abajo y muéstralo al primer conductor disponible.",
                "El trayecto a Chamartín es 14 minutos en coche desde aquí."
            ],
            "afluencia_pct": 0,
            "ruido_db": 38,
            "retraso_minutos": 25,
            "viable": True
        },
        {
            "id": "contingencia_aglomeracion_cercanias",
            "tipo_incidencia": "Aglomeración extrema",
            "incidencia": "Afluencia crítica en L10. Tiempo de espera estimado: +20 min en andén.",
            "pasos": [
                "No bajes al andén. Permanece en superficie ahora mismo.",
                "Dirígete a la estación de Cercanías más cercana (Nuevos Ministerios, 6 min a pie).",
                "Toma Cercanías C4. Vagones centrales — afluencia 35%, aire acondicionado."
            ],
            "afluencia_pct": 35,
            "ruido_db": 52,
            "retraso_minutos": 15,
            "viable": True
        },
        {
            "id": "contingencia_aglomeracion_espera",
            "tipo_incidencia": "Aglomeración extrema",
            "incidencia": "Pico de afluencia detectado. Próximo tren con capacidad normal: 11 min.",
            "pasos": [
                "Retrocede a la zona de acceso. Evita el andén hasta nuevo aviso de esta app.",
                "Espera 11 minutos en la zona de acceso (espacio abierto, menor ruido).",
                "Sube al segundo vagón del próximo tren — afluencia proyectada 28%."
            ],
            "afluencia_pct": 28,
            "ruido_db": 48,
            "retraso_minutos": 11,
            "viable": True
        }
    ]


def obtener_rutas_viables() -> list[RutaContingencia]:
    """
    Devuelve todas las rutas donde viable == True.
    Returns: lista filtrada de RutaContingencia.
    """
    return [r for r in obtener_rutas_contingencia() if r["viable"] is True]


def obtener_rutas_por_tipo(tipo_incidencia: str) -> list[RutaContingencia]:
    """
    Filtra rutas viables por tipo de incidencia.
    Inputs: tipo_incidencia — string exacto del tipo (ver config.TIPOS_INCIDENCIA).
    Returns: lista de rutas viables que coinciden con el tipo.
    """
    return [
        r for r in obtener_rutas_viables()
        if r["tipo_incidencia"] == tipo_incidencia
    ]
