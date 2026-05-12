"""
components.py — Bloques visuales reutilizables. Un componente por función.
"""

import streamlit as st
from config import CONDICION_SENSORIAL_HOY, CONDICION_SENSORIAL_DETALLE

def render_encabezado_sistema() -> None:
    """Renderiza el logo (Flecha de Navegación) y el nombre del sistema."""
    logo_svg = """
    <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 12px;">
        <svg viewBox="0 0 400 400" width="56" height="56" xmlns="http://www.w3.org/2000/svg">
            <rect x="40" y="140" width="160" height="120" rx="8" fill="#528DAB"/>
            <polygon points="180,60 360,200 180,340" fill="#0A1F44"/>
            <circle cx="100" cy="200" r="16" fill="#87C39A"/>
        </svg>
        <div style="display: flex; flex-direction: column;">
            <span style="font-family: 'Instrument Sans', sans-serif; font-size: 32px; font-weight: 700; color: #0A1F44; letter-spacing: -0.02em; line-height: 1;">Navify</span>
            <span style="color: #528DAB; font-size: 12px; letter-spacing: 2px; text-transform: uppercase; font-weight: bold; margin-top: 4px;">SISTEMA DE RUTEO</span>
        </div>
    </div>
    """
    st.markdown(logo_svg, unsafe_allow_html=True)

def render_sensory_check() -> None:
    """Bloque de condición sensorial. Ahora es un panel Azul Principal sólido."""
    st.markdown(
        f"""<div style="background-color: #0A1F44; padding: 16px 20px; margin-bottom: 24px; border-radius: 6px; font-size: 14px; color: #E6FCFB; box-shadow: 0 4px 6px rgba(10,31,68,0.15);">
            <strong style="color: #87C39A; font-size: 12px; text-transform: uppercase; letter-spacing: 1px;">Condición sensorial de hoy</strong><br>
            {CONDICION_SENSORIAL_HOY} — {CONDICION_SENSORIAL_DETALLE}
        </div>""",
        unsafe_allow_html=True
    )

def render_estado_nominal(origen: str, ruta: str, afluencia_pct: int, ruido_db: int) -> None:
    """Renderiza el estado nominal incluyendo el Punto de Origen."""
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
    
    origen_texto = origen if origen else "Estación actual (Detectada)"
    
    st.markdown(
        f"""<div class="metric-container">
            <strong style="color: #0A1F44; font-size: 16px;">📍 Origen:</strong> <span style="font-size: 16px;">{origen_texto}</span><br><br>
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
    color_num = "#87C39A" if completado else "#0A1F44"
    st.markdown(
        f"""<div class="{clase_box}">
            <span class="{clase_num}" style="color: {color_num}; font-weight: bold; margin-right: 12px; font-family: monospace; font-size: 18px;">[{numero}]{marca}</span> {texto}
        </div>""",
        unsafe_allow_html=True
    )

def render_metricas_entorno(afluencia: str, ruido: str, retraso: str) -> None:
    """Renderiza métricas sensoriales de la ruta calculada."""
    st.markdown(
        f"""<div class="metric-container" style="border-left-color:#87C39A; margin-top:20px;">
            <span style="color:#0A1F44; font-weight:bold; font-size:11px; text-transform:uppercase; letter-spacing:1px;">
                Métricas del Plan B
            </span><br>
            <strong>Afluencia estimada:</strong> {afluencia}<br>
            <strong>Nivel de ruido:</strong> {ruido}<br>
            <strong>Impacto en tiempo:</strong> {retraso}
        </div>""",
        unsafe_allow_html=True
    )
