"""
home.py — Página de estado nominal. Selector de origen, ruta y anomalías.
"""

import time
import streamlit as st
from config import (
    RUTAS_DISPONIBLES, RUTA_DEMO_DEFAULT,
    RUTA_DEMO_AFLUENCIA_PCT, RUTA_DEMO_RUIDO_DB,
    TIPOS_INCIDENCIA, TIPO_INCIDENCIA_DEFAULT,
    LABEL_BOTON_INCIDENCIA, LABEL_ESTADO_NOMINAL,
    LABEL_SPINNER_CALCULO, LABEL_ERROR_SIN_RUTAS,
    LABEL_EMPTY_SELECTOR
)
from logic.contingency import generar_plan_b
from logic.validator import ErrorValidacion
from ui.components import (
    render_encabezado_sistema,
    render_sensory_check,
    render_estado_nominal
)

def _activar_panico(tipo_incidencia: str) -> None:
    try:
        with st.spinner(LABEL_SPINNER_CALCULO):
            time.sleep(1.2)
            plan = generar_plan_b(tipo_incidencia)
        st.session_state.panic_mode = True
        st.session_state.plan_b = plan
        st.session_state.pasos_completados = []
    except ErrorValidacion:
        st.error(LABEL_ERROR_SIN_RUTAS)
    except Exception as e:
        st.error(f"Error al calcular ruta alternativa: {e}. Intenta con otro tipo de incidencia.")

def render_home() -> None:
    render_encabezado_sistema()
    render_sensory_check()

    st.markdown(f"<h3 style='color: #0A1F44; font-weight: 700; margin-top: 24px;'>CONFIGURAR VIAJE</h3>", unsafe_allow_html=True)
    
    # Nuevo: Input para el Origen
    origen = st.text_input(
        "Punto de Origen (Estación actual)", 
        placeholder="Ej. Puerta del Sol",
        help="¿Dónde te encuentras ahora mismo?"
    )

    ruta_seleccionada = st.selectbox(
        "Ruta activa / Destino",
        options=[""] + RUTAS_DISPONIBLES,
        index=RUTAS_DISPONIBLES.index(RUTA_DEMO_DEFAULT) + 1,
        help="Selecciona la línea o ruta que vas a tomar."
    )

    if not ruta_seleccionada:
        st.info("Ingresa tu origen y selecciona tu ruta para comenzar a monitorear.")
        return

    # Pasamos el "origen" escrito al componente que lo pinta
    render_estado_nominal(origen, ruta_seleccionada, RUTA_DEMO_AFLUENCIA_PCT, RUTA_DEMO_RUIDO_DB)
    st.markdown("<hr style='border-top: 2px solid #528DAB; margin: 24px 0;'>", unsafe_allow_html=True)

    st.markdown(f"<h3 style='color: #F1B28E; font-weight: 700;'>REPORTE DE ANOMALÍAS</h3>", unsafe_allow_html=True)
    tipo = st.selectbox(
        "¿Qué anomalía se ha detectado?",
        options=TIPOS_INCIDENCIA,
        index=0,
        help="Elige el tipo que coincida con lo que ves en pantalla o megafonía."
    )

    st.write("")

    if st.button(LABEL_BOTON_INCIDENCIA):
        _activar_panico(tipo)
        if st.session_state.get("panic_mode"):
            st.rerun()
