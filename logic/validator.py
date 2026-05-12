"""
validator.py — Validación de inputs en cada frontera del sistema.
Todas las funciones son puras. Sin I/O, sin Streamlit, sin side effects.
Falla rápido con mensajes específicos — nunca en silencio.
"""


class ErrorValidacion(Exception):
    """Error específico de validación de inputs del sistema."""
    pass


def validar_lista_rutas(rutas: list) -> None:
    """
    Verifica que la lista de rutas no esté vacía y tenga estructura mínima.
    Inputs: rutas — lista de dicts de contingencia.
    Outputs: None si válido.
    Errors: ErrorValidacion con mensaje específico si falla.
    """
    if not isinstance(rutas, list):
        raise ErrorValidacion(
            f"Se esperaba una lista de rutas, se recibió: {type(rutas).__name__}."
        )
    if len(rutas) == 0:
        raise ErrorValidacion(
            "La lista de rutas de contingencia está vacía. "
            "Verifica el repositorio en /data/routes.py."
        )


def validar_estructura_ruta(ruta: dict) -> None:
    """
    Verifica que una ruta tenga todos los campos requeridos y tipos correctos.
    Inputs: ruta — dict con campos de RutaContingencia.
    Outputs: None si válido.
    Errors: ErrorValidacion con campo faltante o tipo incorrecto.
    """
    campos_requeridos = {
        "id": str,
        "incidencia": str,
        "pasos": list,
        "afluencia_pct": int,
        "ruido_db": int,
        "retraso_minutos": int,
        "viable": bool
    }

    for campo, tipo_esperado in campos_requeridos.items():
        if campo not in ruta:
            raise ErrorValidacion(
                f"Campo requerido '{campo}' ausente en la ruta '{ruta.get('id', 'sin-id')}'."
            )
        if not isinstance(ruta[campo], tipo_esperado):
            raise ErrorValidacion(
                f"Campo '{campo}' debe ser {tipo_esperado.__name__}, "
                f"recibido: {type(ruta[campo]).__name__}."
            )

    if len(ruta["pasos"]) == 0:
        raise ErrorValidacion(
            f"La ruta '{ruta['id']}' tiene una lista de pasos vacía."
        )

    if not ruta["incidencia"].strip():
        raise ErrorValidacion(
            f"La ruta '{ruta['id']}' tiene una descripción de incidencia vacía."
        )
