"""
components.py — Bloques visuales reutilizables. Un componente por función.
"""

import streamlit as st
from config import (
    COLOR_GOLD, COLOR_MUTED,
    APP_SUBTITLE, CONDICION_SENSORIAL_HOY, CONDICION_SENSORIAL_DETALLE
)


def render_encabezado_sistema() -> None:
    """Renderiza el subtítulo del sistema en la parte superior de cada página."""
    st.markdown(f"<p class='system-subtitle'>{APP_SUBTITLE}</p>", unsafe_allow_html=True)


def render_sensory_check() -> None:
    """Bloque de condición sensorial del día. Dato fijo en demo."""
    st.markdown(
        f"""<div class="sensory-check">
            <strong>Condición sensorial hoy</strong><br>
            {CONDICION_SENSORIAL_HOY} — {CONDICION_SENSORIAL_DETALLE}
        </div>""",
        unsafe_allow_html=True
    )


def render_estado_nominal(ruta: str, afluencia_pct: int, ruido_db: int) -> None:
    """
    Renderiza el estado nominal del viaje con pills de severidad.
    Inputs: ruta — nombre de la ruta. afluencia_pct — %. ruido_db — decibeles.
    """
    pill_a = (
        "<span class='pill pill-alert'>Alta</span>" if afluencia_pct >= 70
        else "<span class='pill pill-warn'>Media</span>" if afluencia_pct >= 45
        else "<span class='pill pill-ok'>Baja</span>"
    )
    pill_r = (
        "<span class='pill pill-alert'>Alto</span>" if ruido_db >= 75
        else "<span class='pill pill-warn'>Medio</span>" if ruido_db >= 60
        else "<span class='pill pill-ok'>Bajo</span>"
    )
    st.markdown(
        f"""<div class="metric-container">
            <strong>Ruta activa:</strong> {ruta}<br>
            <strong>Afluencia actual:</strong> {afluencia_pct}% {pill_a}<br>
            <strong>Nivel de ruido:</strong> {ruido_db} dB {pill_r}
        </div>""",
        unsafe_allow_html=True
    )


def render_step_box(numero: int, texto: str, completado: bool = False) -> None:
    """
    Renderiza un paso numerado del Plan B.
    Inputs: numero — 1-based. texto — instrucción literal. completado — resalta como hecho.
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
    Renderiza métricas sensoriales de la ruta calculada.
    Inputs: etiquetas ya formateadas desde /logic/contingency.py.
    """
    st.markdown(
        f"""<div class="metric-container" style="border-left-color:#F9E795; margin-top:20px;">
            <span style="color:#F9E795; font-weight:bold; font-size:11px;
                  text-transform:uppercase; letter-spacing:1px;">
                Métricas de entorno
            </span><br>
            <strong>Afluencia estimada:</strong> {afluencia}<br>
            <strong>Nivel de ruido:</strong> {ruido}<br>
            <strong>Impacto en tiempo:</strong> {retraso}
        </div>""",
        unsafe_allow_html=True
    )
