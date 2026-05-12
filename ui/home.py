"""
home.py — Página de estado nominal. Selector de ruta + activación de incidencia.
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
    st.markdown(f"<h3 style='color: #0A1F44; font-weight: 700;'>{LABEL_ESTADO_NOMINAL}</h3>", unsafe_allow_html=True)
    render_sensory_check()

    ruta_seleccionada = st.selectbox(
        "Ruta activa",
        options=[""] + RUTAS_DISPONIBLES,
        index=RUTAS_DISPONIBLES.index(RUTA_DEMO_DEFAULT) + 1,
        help="Selecciona la línea que estás usando ahora mismo."
    )

    if not ruta_seleccionada:
        st.info(LABEL_EMPTY_SELECTOR)
        return

    render_estado_nominal(ruta_seleccionada, RUTA_DEMO_AFLUENCIA_PCT, RUTA_DEMO_RUIDO_DB)
    st.markdown("<hr style='border-top: 1px solid rgba(63,79,99,0.2); margin: 20px 0;'>", unsafe_allow_html=True)

    tipo = st.selectbox(
        "Tipo de incidencia detectada",
        options=TIPOS_INCIDENCIA,
        index=0,
        help="Elige el tipo que coincida con lo que ves en pantalla o megafonía."
    )

    st.write("")

    if st.button(LABEL_BOTON_INCIDENCIA):
        _activar_panico(tipo)
        if st.session_state.get("panic_mode"):
            st.rerun()
