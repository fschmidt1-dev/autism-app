"""
_brand.py — Inyección CSS global. Un solo lugar para toda decisión visual.
Importado una sola vez desde app.py. No contiene lógica ni componentes.
"""

import streamlit as st
from config import (
    COLOR_NAVY, COLOR_CORAL, COLOR_GOLD,
    COLOR_TINTA, COLOR_MUTED, COLOR_BG,
    COLOR_SURFACE, COLOR_BORDER
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
    h1, h2, h3, h4, p, span, div {{
        font-family: system-ui, -apple-system, sans-serif !important;
    }}

    /* BOTÓN PRINCIPAL */
    div.stButton > button:first-child {{
        background-color: {COLOR_NAVY};
        color: #FAF7F2;
        border: 2px solid {COLOR_CORAL};
        border-radius: 4px;
        font-weight: bold;
        font-size: 18px;
        padding: 24px;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: background-color 0.2s ease, color 0.2s ease;
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
        padding: 16px;
        margin-bottom: 24px;
        font-size: 14px;
        line-height: 1.6;
    }}

    /* PASO DE PLAN B */
    .step-box {{
        background-color: {COLOR_SURFACE};
        border: 1px solid {COLOR_BORDER};
        padding: 18px;
        margin-bottom: 8px;
        border-radius: 4px;
        font-size: 16px;
        line-height: 1.5;
    }}
    .step-number {{
        color: {COLOR_GOLD};
        font-weight: bold;
        margin-right: 12px;
        font-family: monospace;
    }}

    /* ALERTA DE ANOMALÍA */
    .anomalia-header {{
        color: {COLOR_CORAL};
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 8px;
    }}
    .plan-b-label {{
        color: {COLOR_GOLD};
        font-size: 16px;
        font-weight: bold;
        margin: 24px 0 12px 0;
    }}
    .metricas-label {{
        color: {COLOR_GOLD};
        font-weight: bold;
    }}
</style>
"""


def aplicar_estilos_globales() -> None:
    """
    Inyecta el bloque CSS global en la app de Streamlit.
    Debe llamarse una sola vez desde app.py antes de renderizar cualquier página.
    """
    st.markdown(CSS_GLOBAL, unsafe_allow_html=True)
