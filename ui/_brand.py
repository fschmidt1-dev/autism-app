"""
_brand.py — Sistema de diseño y tokens inyectados vía CSS.
"""
import streamlit as st

def aplicar_estilos_globales():
    css = """
    <style>
    /* IMPORTACIÓN DE FUENTES */
    @import url('https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;600;700&family=Space+Mono:wght@400;700&display=swap');

    /* DESIGN TOKENS */
    :root {
        --c-primary: #0A1F44;
        --c-accent: #87C39A;
        --c-text: #040F2D;
        --c-bg: #FEFDFA;
        --c-surface: #F9FBFD;
        --c-muted: #3F4F63;
        
        --s-sm: 8px;
        --s-md: 16px;
        --s-lg: 24px;
        --r-md: 4px;
        
        --font-body: 'Instrument Sans', sans-serif;
        --font-mono: 'Space Mono', monospace;
    }

    /* TYPOGRAPHY BASE */
    html, body, [class*="st-"] {
        font-family: var(--font-body) !important;
        color: var(--c-text);
    }
    
    h1, h2, h3 {
        font-weight: 700 !important;
        color: var(--c-primary) !important;
        letter-spacing: -0.02em;
    }

    /* DATA & METRICS (MONO) */
    code, .stCodeBlock, [data-testid="stMetricValue"] {
        font-family: var(--font-mono) !important;
    }

    /* STREAMLIT OVERRIDES */
    .stApp {
        background-color: var(--c-bg);
    }
    
    [data-testid="stHeader"] {
        background-color: transparent;
    }

    /* BUTTONS */
    .stButton > button {
        background-color: var(--c-primary) !important;
        color: var(--c-bg) !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        border: none !important;
        border-radius: var(--r-md) !important;
        padding: var(--s-md) var(--s-lg) !important;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        transition: background-color 0.2s ease;
    }
    
    .stButton > button:hover {
        background-color: var(--c-accent) !important;
        color: var(--c-primary) !important;
    }

    /* CARDS & CONTAINERS (UI Components) */
    .step-box {
        background-color: #FFFFFF;
        border-left: 4px solid var(--c-muted);
        padding: var(--s-md);
        margin-bottom: var(--s-sm);
        border-radius: 0 var(--r-md) var(--r-md) 0;
        font-size: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    
    .step-box.completado {
        border-left-color: var(--c-accent);
        opacity: 0.7;
    }

    .metric-container {
        background-color: #FFFFFF;
        border-left: 4px solid var(--c-muted);
        padding: 16px;
        margin-bottom: 24px;
        border-radius: 0 var(--r-md) var(--r-md) 0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    
    /* TOKENS/PILLS */
    .pill {
        display: inline-block;
        padding: 3px 10px;
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

    /* SILENT CARD */
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
        color: var(--c-bg);
        font-size: clamp(28px, 5vw, 48px);
        font-weight: bold;
        line-height: 1.5;
        white-space: pre-line;
    }
    .silent-card-label {
        color: var(--c-accent);
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 32px;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
