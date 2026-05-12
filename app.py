import streamlit as st
import random
import time

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(
    page_title="Ruteo Crítico",
    page_icon="⬛",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. INYECCIÓN CSS (UI SOBRIA Y OSCURA) ---
css = """
<style>
    .stApp {
        background-color: #0E1117;
        color: #E0E6ED;
    }
    header {visibility: hidden;}
    footer {visibility: hidden;}
    h1, h2, h3, h4, p, span {
        font-family: system-ui, -apple-system, sans-serif !important;
    }
    div.stButton > button:first-child {
        background-color: #1E2761;
        color: #FAF7F2;
        border: 2px solid #F96167;
        border-radius: 4px;
        font-weight: bold;
        font-size: 18px;
        padding: 24px;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.2s ease;
    }
    div.stButton > button:hover {
        background-color: #F96167;
        color: #1A1A1A;
        border-color: #F96167;
    }
    .metric-container {
        background-color: #1A1A1A;
        border-left: 4px solid #6B6B6B;
        padding: 16px;
        margin-bottom: 24px;
        font-size: 14px;
        line-height: 1.6;
    }
    .step-box {
        background-color: #1A1A1A;
        border: 1px solid #333333;
        padding: 18px;
        margin-bottom: 8px;
        border-radius: 4px;
        font-size: 16px;
        line-height: 1.5;
    }
    .step-number {
        color: #F9E795;
        font-weight: bold;
        margin-right: 12px;
        font-family: monospace;
    }
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# --- 3. GESTIÓN DE ESTADO ---
if 'panic_mode' not in st.session_state:
    st.session_state.panic_mode = False
if 'plan_b' not in st.session_state:
    st.session_state.plan_b = None
if 'incidencia_cruda' not in st.session_state:
    st.session_state.incidencia_cruda = None

# --- 4. MOTOR LÓGICO (sin pandas — stdlib pura) ---
RUTAS_CONTINGENCIA = [
    {
        "incidencia": "Avería mecánica en L10.",
        "pasos": [
            "Baja en la próxima estación (Tribunal).",
            "Usa la salida Norte (Calle Fuencarral).",
            "Toma el autobús 40 en la acera derecha."
        ],
        "afluencia": "30% (Baja)",
        "ruido": "Bajo (< 60dB)",
        "retraso_total": "+12 minutos"
    },
    {
        "incidencia": "Corte de servicio por aglomeración.",
        "pasos": [
            "No subas al tren. Retrocede a los tornos.",
            "Camina 400 metros al sur hacia Alonso Martínez.",
            "Sube a Línea 5, vagón de cola."
        ],
        "afluencia": "45% (Media)",
        "ruido": "Medio",
        "retraso_total": "+18 minutos"
    }
]

def generar_plan_b():
    with st.spinner("Procesando anomalía. Calculando evasión..."):
        time.sleep(1.2)
        seleccion = random.choice(RUTAS_CONTINGENCIA)
        st.session_state.panic_mode = True
        st.session_state.incidencia_cruda = seleccion["incidencia"]
        st.session_state.plan_b = {
            "pasos": seleccion["pasos"],
            "afluencia": seleccion["afluencia"],
            "ruido": seleccion["ruido"],
            "retraso_total": seleccion["retraso_total"]
        }

def reset_viaje():
    st.session_state.panic_mode = False
    st.session_state.plan_b = None
    st.session_state.incidencia_cruda = None

# --- 5. INTERFAZ ---
st.markdown("<h2 style='color:#6B6B6B; font-size:16px; letter-spacing:2px; text-transform:uppercase;'>SISTEMA DE RUTEO TÁCTICO</h2>", unsafe_allow_html=True)

if not st.session_state.panic_mode:
    st.markdown("### ESTADO: VIAJE EN CURSO")
    st.markdown("""
    <div class="metric-container">
        <strong>Ruta:</strong> L10 Norte<br>
        <strong>Destino final:</strong> Chamartín<br>
        <strong>Densidad actual:</strong> 65% (Aceptable)
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    if st.button("INCIDENCIA DETECTADA · RECALCULAR"):
        generar_plan_b()
        st.rerun()

else:
    plan = st.session_state.plan_b
    st.markdown(f"<h3 style='color:#F96167;'>ANOMALÍA: {st.session_state.incidencia_cruda}</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='margin-top: 24px; margin-bottom: 12px; color:#F9E795;'>PLAN B ACTIVO:</h4>", unsafe_allow_html=True)

    for i, paso in enumerate(plan["pasos"]):
        st.markdown(f"""
        <div class="step-box">
            <span class="step-number">[{i+1}]</span> {paso}
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="metric-container" style="margin-top: 24px; border-left-color: #F9E795;">
        <strong style="color:#F9E795;">MÉTRICAS DE ENTORNO:</strong><br>
        Afluencia estimada: {plan['afluencia']}<br>
        Ruido estimado: {plan['ruido']}<br>
        Impacto en tiempo: {plan['retraso_total']}
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    if st.button("VIAJE COMPLETADO · RESETEAR"):
        reset_viaje()
        st.rerun()
