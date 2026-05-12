"""
_brand.py — Sistema de diseño y tokens inyectados vía CSS.
Debe ser llamado en la primera línea renderizable de cada vista.
"""
import streamlit as st

def inject_brand():
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
        --c-alert: #F1B28E;
        
        --s-xs: 4px;
        --s-sm: 8px;
        --s-md: 16px;
        --s-lg: 24px;
        --s-xl: 32px;
        
        --r-sm: 2px;
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

    /* STREAMLIT OVERRIDES: APP & SURFACE */
    .stApp {
        background-color: var(--c-bg);
    }
    
    [data-testid="stHeader"] {
        background-color: transparent;
    }

    /* CARDS & CONTAINERS */
    div[data-testid="stVerticalBlock"] > div[style*="flex-direction: column"] {
        background-color: var(--c-surface);
        padding: var(--s-lg);
        border-radius: var(--r-md);
        border: 1px solid rgba(63, 79, 99, 0.1);
        box-shadow: 0 4px 6px rgba(4, 15, 45, 0.04);
    }

    /* INPUTS */
    .stTextInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        border: 1px solid rgba(63, 79, 99, 0.2) !important;
        border-radius: var(--r-md) !important;
        font-family: var(--font-body);
        color: var(--c-text) !important;
        transition: border-color 0.2s ease;
    }
    .stTextInput input:focus, .stSelectbox div[data-baseweb="select"]:focus-within {
        border-color: var(--c-primary) !important;
        box-shadow: 0 0 0 1px var(--c-primary) !important;
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
    
    .stButton > button:active {
        transform: translateY(1px);
    }

    /* CUSTOM UTILITY CLASSES FOR UI MODULES */
    .navify-step-box {
        background-color: #FFFFFF;
        border-left: 4px solid var(--c-muted);
        padding: var(--s-md);
        margin-bottom: var(--s-sm);
        border-radius: 0 var(--r-md) var(--r-md) 0;
        font-size: 16px;
    }
    
    .navify-step-box.completed {
        border-left-color: var(--c-accent);
        opacity: 0.7;
    }
    
    .navify-mono-metric {
        font-family: var(--font-mono);
        font-size: 14px;
        color: var(--c-muted);
        display: block;
        margin-top: var(--s-xs);
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
