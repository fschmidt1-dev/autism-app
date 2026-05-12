"""
_brand.py — Sistema de diseño y tokens inyectados vía CSS.
"""
import streamlit as st

def aplicar_estilos_globales():
    css = """
    <style>
    /* IMPORTACIÓN DE FUENTES */
    @import url('https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;600;700&family=Space+Mono:wght@400;700&display=swap');

    :root {
        --c-primary: #0A1F44; /* AZUL PRINCIPAL */
        --c-primary-dark: #040F2D;
        --c-accent: #87C39A;
        --c-text: #040F2D;
        --c-bg: #FEFDFA;
        
        --font-body: 'Instrument Sans', sans-serif;
        --font-mono: 'Space Mono', monospace;
    }

    html, body, [class*="st-"] {
        font-family: var(--font-body) !important;
        color: var(--c-text);
    }
    
    h1, h2, h3 {
        font-weight: 700 !important;
        color: var(--c-primary) !important;
        letter-spacing: -0.02em;
    }

    .stApp {
        background-color: var(--c-bg);
    }
    
    [data-testid="stHeader"] {
        background-color: transparent;
    }

    /* ARREGLO DE BOTONES: Texto blanco, fondo azul principal */
    div.stButton > button {
        background-color: var(--c-primary) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        border: 2px solid var(--c-primary-dark) !important;
        border-radius: 6px !important;
        padding: 24px !important;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    div.stButton > button:hover {
        background-color: var(--c-accent) !important;
        color: var(--c-primary-dark) !important;
        border-color: var(--c-accent) !important;
    }
    
    /* Streamlit a veces esconde el texto en una etiqueta <p>, esto lo fuerza a obedecer */
    div.stButton > button p {
        color: inherit !important; 
    }

    /* CAJAS DE INFORMACIÓN (Más Azul Principal) */
    .step-box {
        background-color: #FFFFFF;
        border-left: 6px solid var(--c-primary); 
        padding: 16px;
        margin-bottom: 8px;
        border-radius: 0 4px 4px 0;
        font-size: 16px;
        box-shadow: 0 2px 4px rgba(10,31,68,0.1);
    }
    
    .step-box.completado {
        border-left-color: var(--c-accent);
        opacity: 0.7;
    }

    .metric-container {
        background-color: #FFFFFF;
        border: 2px solid var(--c-primary); 
        padding: 16px 20px;
        margin-bottom: 24px;
        border-radius: 6px;
        box-shadow: 0 4px 8px rgba(10,31,68,0.05);
    }
    
    /* INPUTS */
    .stTextInput input, .stSelectbox div[data-baseweb="select"] {
        border: 2px solid #528DAB !important;
        border-radius: 4px !important;
        color: var(--c-primary-dark) !important;
    }

    /* PILLS DE ESTADO */
    .pill {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: bold;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        margin-left: 8px;
    }
    .pill-ok { background-color: #E6FCFB; color: #528DAB; }
    .pill-warn { background-color: #FEF6E9; color: #F1B28E; }
    .pill-alert { background-color: #FEF2EA; color: #F89F97; }

    /* TARJETA DE SILENCIO */
    .silent-card-container {
        background-color: var(--c-primary);
        min-height: 70vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 48px 32px;
        border-radius: 8px;
        text-align: center;
    }
    .silent-card-text {
        color: #FFFFFF;
        font-size: clamp(28px, 5vw, 48px);
        font-weight: bold;
        line-height: 1.5;
        white-space: pre-line;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
