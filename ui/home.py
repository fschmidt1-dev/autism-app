"""
home.py — Página de estado nominal del viaje.
Solo renderiza. Importa de /logic/ y /ui/components.py. Sin reglas de negocio.
"""

import time
import streamlit as st
from config import (
    RUTA_DEMO_NOMBRE, RUTA_DEMO_DESTINO, RUTA_DEMO_AFLUENCIA_PCT,
    LABEL_BOTON_INCIDENCIA, LABEL_ESTADO_NOMINAL, SPINNER_DELAY_SEGUNDOS
)
from logic.contingency import generar_plan_b
from logic.validator import ErrorValidacion
from ui.components import render_encabezado_sistema, render_estado_nominal


def _activar_panico() -> None:
    """
    Llama al motor lógico para generar Plan B y persiste resultado en session_state.
    Envuelve la llamada externa en try/except con mensaje específico.
    """
    try:
        with st.spinner("Procesando anomalía. Calculando evasión..."):
            time.sleep(SPINNER_DELAY_SEGUNDOS)
            plan = generar_plan_b()

        st.session_state.panic_mode = True
        st.session_state.plan_b = plan

    except ErrorValidacion as e:
        st.error(f"Error en datos de rutas: {e}")
    except Exception as e:
        st.error(f"Error inesperado al calcular Plan B: {e}")


def render_home() -> None:
    """
    Renderiza la página de estado nominal.
    Muestra ruta activa y el botón de activación de incidencia.
    """
    render_encabezado_sistema()
    st.markdown(f"### {LABEL_ESTADO_NOMINAL}")
    render_estado_nominal(RUTA_DEMO_NOMBRE, RUTA_DEMO_DESTINO, RUTA_DEMO_AFLUENCIA_PCT)

    st.write("")
    if st.button(LABEL_BOTON_INCIDENCIA):
        _activar_panico()
        st.rerun()
