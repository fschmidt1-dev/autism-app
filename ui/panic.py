"""
panic.py — Página de Plan B activo post-incidencia.
Renderiza los datos calculados en /logic/. Sin cálculos propios.
"""

import streamlit as st
from config import (
    COLOR_CORAL, LABEL_BOTON_RESET,
    LABEL_PLAN_B_ACTIVO
)
from ui.components import (
    render_encabezado_sistema,
    render_step_box,
    render_metricas_entorno
)


def _resetear_viaje() -> None:
    """Limpia el estado de sesión para volver al estado nominal."""
    st.session_state.panic_mode = False
    st.session_state.plan_b = None


def render_panic() -> None:
    """
    Renderiza la pantalla de contingencia con Plan B activo.
    Lee datos desde st.session_state.plan_b — nunca los recalcula.
    """
    render_encabezado_sistema()

    plan = st.session_state.plan_b

    if plan is None:
        st.error("Error de estado: Plan B no disponible. Reinicia el viaje.")
        if st.button(LABEL_BOTON_RESET):
            _resetear_viaje()
            st.rerun()
        return

    # Encabezado de anomalía
    st.markdown(
        f"<div class='anomalia-header'>ANOMALÍA: {plan['incidencia']}</div>",
        unsafe_allow_html=True
    )

    # Pasos del Plan B
    st.markdown(
        f"<div class='plan-b-label'>{LABEL_PLAN_B_ACTIVO}</div>",
        unsafe_allow_html=True
    )
    for i, paso in enumerate(plan["pasos"]):
        render_step_box(numero=i + 1, texto=paso)

    # Métricas sensoriales
    render_metricas_entorno(
        afluencia=plan["afluencia_label"],
        ruido=plan["ruido_label"],
        retraso=plan["retraso_label"]
    )

    st.write("")
    if st.button(LABEL_BOTON_RESET):
        _resetear_viaje()
        st.rerun()
