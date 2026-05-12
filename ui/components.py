"""
components.py — Bloques visuales reutilizables.
Cada función renderiza UN componente específico. Sin lógica de negocio.
"""

import streamlit as st
from config import COLOR_GOLD, COLOR_MUTED, APP_SUBTITLE


def render_encabezado_sistema() -> None:
    """Renderiza el título del sistema en la parte superior de cada página."""
    st.markdown(
        f"<h2 style='color:{COLOR_MUTED}; font-size:16px; "
        f"letter-spacing:2px; text-transform:uppercase;'>"
        f"{APP_SUBTITLE}</h2>",
        unsafe_allow_html=True
    )


def render_step_box(numero: int, texto: str) -> None:
    """
    Renderiza un paso numerado de Plan B.
    Inputs: numero — entero del paso (1-based). texto — instrucción literal.
    """
    st.markdown(
        f"""<div class="step-box">
            <span class="step-number">[{numero}]</span> {texto}
        </div>""",
        unsafe_allow_html=True
    )


def render_metricas_entorno(afluencia: str, ruido: str, retraso: str) -> None:
    """
    Renderiza el bloque de métricas sensoriales de una ruta.
    Inputs: afluencia — label de afluencia. ruido — label de ruido. retraso — label de tiempo.
    """
    st.markdown(
        f"""<div class="metric-container" style="border-left-color:{COLOR_GOLD}; margin-top:24px;">
            <span class="metricas-label">MÉTRICAS DE ENTORNO:</span><br>
            Afluencia estimada: {afluencia}<br>
            Ruido estimado: {ruido}<br>
            Impacto en tiempo: {retraso}
        </div>""",
        unsafe_allow_html=True
    )


def render_estado_nominal(ruta: str, destino: str, afluencia_pct: int) -> None:
    """
    Renderiza el bloque de estado nominal del viaje.
    Inputs: ruta — nombre de la ruta activa. destino — estación final. afluencia_pct — ocupación actual.
    """
    st.markdown(
        f"""<div class="metric-container">
            <strong>Ruta:</strong> {ruta}<br>
            <strong>Destino final:</strong> {destino}<br>
            <strong>Densidad actual:</strong> {afluencia_pct}% (Aceptable)
        </div>""",
        unsafe_allow_html=True
    )
