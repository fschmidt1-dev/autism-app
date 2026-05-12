"""
components.py — Bloques visuales reutilizables. Un componente por función.
"""

import streamlit as st
from config import CONDICION_SENSORIAL_HOY, CONDICION_SENSORIAL_DETALLE

def render_encabezado_sistema() -> None:
    """Renderiza el logo y el subtítulo del sistema en la parte superior."""
    logo_svg = """
    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
        <svg viewBox="0 0 400 400" width="36" height="36" xmlns="http://www.w3.org/2000/svg">
            <g transform="translate(130, 100)">
                <rect x="0" y="0" width="40" height="200" rx="6" fill="#528DAB"/>
                <rect x="100" y="0" width="40" height="200" rx="6" fill="#528DAB"/>
                <circle cx="70" cy="100" r="26" fill="#87C39A"/>
            </g>
        </svg>
        <span style="font-family: 'Instrument Sans', sans-serif; font-size: 28px; font-weight: 700; color: #0A1F44; letter-spacing: -0.02em;">Navify</span>
    </div>
    """
    st.markdown(logo_svg, unsafe_allow_html=True)
    st.markdown("<p class='system-subtitle' style='color: #3F4F63; font-size: 13px; letter-spacing: 2px; text-transform: uppercase; margin-top: 0;'>SISTEMA DE RUTEO TÁCTICO</p>", unsafe_allow_html=True)

def render_sensory_check() -> None:
    """Bloque de condición sensorial del día."""
    st.markdown(
        f"""<div class="sensory-check" style="background-color: #FFFFFF; border: 1px solid rgba(63,79,99,0.2); border-top: 3px solid #87C39A; padding: 14px 18px; margin-bottom: 20px; border-radius: 4px; font-size: 13px; color: #3F4F63;">
            <strong style="color: #0A1F44; font-size: 11px; text-transform: uppercase; letter-spacing: 1px;">Condición sensorial hoy</strong><br>
            {CONDICION_SENSORIAL_HOY} — {CONDICION_SENSORIAL_DETALLE}
        </div>""",
        unsafe_allow_html=True
    )

def render_estado_nominal(ruta: str, afluencia_pct: int, ruido_db: int) -> None:
    """Renderiza el estado nominal del viaje con pills de severidad."""
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
    """Renderiza un paso numerado del Plan B."""
    clase_box = "step-box completado" if completado else "step-box"
    clase_num = "step-number completado" if completado else "step-number"
    marca = " ✓" if completado else ""
    st.markdown(
        f"""<div class="{clase_box}">
            <span class="{clase_num}" style="color: #87C39A; font-weight: bold; margin-right: 12px; font-family: monospace;">[{numero}]{marca}</span> {texto}
        </div>""",
        unsafe_allow_html=True
    )

def render_metricas_entorno(afluencia: str, ruido: str, retraso: str) -> None:
    """Renderiza métricas sensoriales de la ruta calculada."""
    st.markdown(
        f"""<div class="metric-container" style="border-left-color:#87C39A; margin-top:20px;">
            <span style="color:#0A1F44; font-weight:bold; font-size:11px; text-transform:uppercase; letter-spacing:1px;">
                Métricas de entorno
            </span><br>
            <strong>Afluencia estimada:</strong> {afluencia}<br>
            <strong>Nivel de ruido:</strong> {ruido}<br>
            <strong>Impacto en tiempo:</strong> {retraso}
        </div>""",
        unsafe_allow_html=True
    )
