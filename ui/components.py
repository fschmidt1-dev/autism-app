"""
components.py — Bloques visuales reutilizables.
Cada función renderiza UN componente. Sin lógica de negocio.
"""

import streamlit as st
from config import (
    COLOR_GOLD, COLOR_MUTED, COLOR_SUCCESS,
    APP_SUBTITLE, CONDICION_SENSORIAL_HOY, CONDICION_SENSORIAL_DETALLE
)


def render_encabezado_sistema() -> None:
    """Renderiza el subtítulo del sistema en la parte superior de cada página."""
    st.markdown(
        f"<p class='system-subtitle'>{APP_SUBTITLE}</p>",
        unsafe_allow_html=True
    )


def render_sensory_check() -> None:
    """
    Renderiza el bloque de condición sensorial del día.
    Datos fijos en demo; en producción se conectarían a APIs de tráfico.
    """
    st.markdown(
        f"""<div class="sensory-check">
            <strong>Condición sensorial hoy</strong><br>
            {CONDICION_SENSORIAL_HOY} — {CONDICION_SENSORIAL_DETALLE}
        </div>""",
        unsafe_allow_html=True
    )


def render_estado_nominal(ruta: str, afluencia_pct: int, ruido_db: int) -> None:
    """
    Renderiza el bloque de estado nominal del viaje.
    Inputs: ruta — nombre de la ruta activa. afluencia_pct — ocupación. ruido_db — nivel de ruido.
    """
    if afluencia_pct >= 70:
        pill_afluencia = "<span class='pill pill-alert'>Alta</span>"
    elif afluencia_pct >= 45:
        pill_afluencia = "<span class='pill pill-warn'>Media</span>"
    else:
        pill_afluencia = "<span class='pill pill-ok'>Baja</span>"

    if ruido_db >= 75:
        pill_ruido = "<span class='pill pill-alert'>Alto</span>"
    elif ruido_db >= 60:
        pill_ruido = "<span class='pill pill-warn'>Medio</span>"
    else:
        pill_ruido = "<span class='pill pill-ok'>Bajo</span>"

    st.markdown(
        f"""<div class="metric-container">
            <strong>Ruta activa:</strong> {ruta}<br>
            <strong>Afluencia actual:</strong> {afluencia_pct}% {pill_afluencia}<br>
            <strong>Nivel de ruido:</strong> {ruido_db} dB {pill_ruido}
        </div>""",
        unsafe_allow_html=True
    )


def render_step_box(numero: int, texto: str, completado: bool = False) -> None:
    """
    Renderiza un paso numerado de Plan B, con estado de completado opcional.
    Inputs: numero — entero 1-based. texto — instrucción literal. completado — bool.
    """
    clase_box = "step-box completado" if completado else "step-box"
    clase_num = "step-number completado" if completado else "step-number"
    marca = " ✓" if completado else ""

    st.markdown(
        f"""<div class="{clase_box}">
            <span class="{clase_num}">[{numero}]{marca}</span> {texto}
        </div>""",
        unsafe_allow_html=True
    )


def render_metricas_entorno(afluencia: str, ruido: str, retraso: str) -> None:
    """
    Renderiza el bloque de métricas sensoriales post-cálculo.
    Inputs: afluencia, ruido, retr
