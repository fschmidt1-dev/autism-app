"""
_brand.py — Inyección CSS global. Toda decisión visual en un solo lugar.
"""

import streamlit as st
from config import (
    COLOR_NAVY, COLOR_CORAL, COLOR_GOLD,
    COLOR_TINTA, COLOR_MUTED, COLOR_BG,
    COLOR_SURFACE, COLOR_BORDER, COLOR_SUCCESS
)

CSS_GLOBAL = f"""
<style>
    /* BASE */
    .stApp {{
        background-color: {COLOR_BG};
        color: #E0E6ED;
    }}
    header {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    * {{
        font-family: system-ui, -apple-system, sans-serif !important;
    }}

    /* BOTÓN PRINCIPAL */
    div.stButton > button:first-child {{
        background-color: {COLOR_NAVY};
        color: #FAF7F2;
        border: 2px solid {COLOR_CORAL};
        border-radius: 4px;
        font-weight: bold;
        font-size: 16px;
        padding: 20px;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: background-color 0.2s ease, color 0.2s ease;
        cursor: pointer;
    }}
    div.stButton > button:hover {{
        background-color: {COLOR_CORAL};
        color: {COLOR_TINTA};
        border-color: {COLOR_CORAL};
    }}

    /* CONTENEDOR DE DATOS */
    .metric-container {{
        background-color: {COLOR_SURFACE};
        border-left: 4px solid {COLOR_MUTED};
        padding: 16px 20px;
        margin-bottom: 16px;
        font-size: 14px;
        line-height: 1.8;
        border-radius: 2px;
    }}

    /* PASO DE PLAN B */
    .step-box {{
        background-color: {COLOR_SURFACE};
        border: 1px solid {COLOR_BORDER};
        padding: 16px 20px;
        margin-bottom: 8px;
        border-radius: 4px;
        font-size: 15px;
        line-height: 1.6;
    }}
    .step-box.completado {{
        border-color: {COLOR_SUCCESS};
        opacity: 0.65;
    }}
    .step-number {{
        color: {COLOR_GOLD};
        font-weight: bold;
        margin-right: 12px;
        font-family: monospace;
    }}
    .step-number.completado {{
        color: {COLOR_SUCCESS};
    }}

    /* STATUS PILLS */
    .pill {{
        display: inline-block;
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: bold;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        margin-left: 8px;
    }}
    .pill-ok {{ background-color: #1A3A2A; color: {COLOR_SUCCESS}; }}
    .pill-warn {{ background-color: #3A2A1A; color: {COLOR_GOLD}; }}
    .pill-alert {{ background-color: #3A1A1A; color: {COLOR_CORAL}; }}

    /* ANOMALÍA HEADER */
    .anomalia-header {{
        color: {COLOR_CORAL};
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 6px;
        line-height: 1.4;
    }}
    .plan-b-label {{
        color: {COLOR_GOLD};
        font-size: 15px;
        font-weight: bold;
        margin: 20px 0 10px 0;
        letter-spacing: 0.5px;
    }}

    /* SENSORY CHECK */
    .sensory-check {{
        background-color: {COLOR_SURFACE};
        border: 1px solid {COLOR_BORDER};
        border-top: 3px solid {COLOR_GOLD};
        padding: 14px 18px;
        margin-bottom: 20px;
        border-radius: 2px;
        font-size: 13px;
        line-height: 1.7;
        color: {COLOR_MUTED};
    }}
    .sensory-check strong {{
        color: {COLOR_GOLD};
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}

    /* SILENT CARD */
    .silent-card-container {{
        background-color: #000000;
        min-height: 70vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 48px 32px;
        border-radius: 4px;
        text-align: center;
    }}
    .silent-card-text {{
        color: #FFFFFF;
        font-size: clamp(28px, 5vw, 48px);
        font-weight: bold;
        line-height: 1.5;
        white-space: pre-line;
    }}
    .silent-card-label {{
        color: {COLOR_MUTED};
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 32px;
    }}

    /* SUBTÍTULO DEL SISTEMA */
    .system-subtitle {{
        color: {COLOR_MUTED};
        font-size: 13px;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 4px;
    }}
    .divider {{
        border: none;
        border-top: 1px solid {COLOR_BORDER};
        margin: 20px 0;
    }}
</style>
"""


def aplicar_estilos_globales() -> None:
    """
    Inyecta el bloque CSS global. Llamar una sola vez desde app.py.
    """
    st.markdown(CSS_GLOBAL, unsafe_allow_html=True)
