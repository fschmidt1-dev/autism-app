"""
panic.py — Página de Plan B activo. Renderiza datos del session_state.
Incluye paso-a-paso táctil y trigger al modo silencioso.
"""

import streamlit as st
from config import (
    COLOR_CORAL, COLOR_GOLD,
    LABEL_BOTON_RESET, LABEL_BOTON_SILENT,
    LABEL_PLAN_B_ACTIVO, LABEL_TOAST_RESET
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
    st.session_state.silent_mode = False
    st.session_state.pasos_completados = []


def render_panic() -> None:
    """
    Renderiza la pantalla de contingencia con Plan B activo.
    Estados: ERROR (plan_b None) · SUCCESS (pasos completados) · NORMAL.
    """
    render_encabezado_sistema()
    plan = st.session_state.get("plan_b")

    # Estado ERROR — plan_b no disponible
    if plan is None:
        st.error("Estado inconsistente: Plan B no disponible. Reinicia el viaje.")
        if st.button(LABEL_BOTON_RESET):
            _resetear_viaje()
            st.rerun()
        return

    # Encabezado de anomalía
    st.markdown(
        f"<div class='anomalia-header'>ANOMALÍA DETECTADA:<br>{plan['incidencia']}</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<div class='plan-b-label'>{LABEL_PLAN_B_ACTIVO}</div>",
        unsafe_allow_html=True
    )

    # Pasos con checkboxes táctiles para marcar progreso
    pasos_completados = st.session_state.get("pasos_completados", [])
    for i, paso in enumerate(plan["pasos"]):
        col_check, col_texto = st.columns([0.08, 0.92])
        with col_check:
            marcado = st.checkbox(
                label="hecho",
                value=(i in pasos_completados),
                key=f"paso_{i}",
                label_visibility="collapsed"
            )
            if marcado and i not in pasos_completados:
                pasos_completados.append(i)
                st.session_state.pasos_completados = pasos_completados
        with col_texto:
            render_step_box(i + 1, paso, completado=(i in pasos_completados))

    # Estado SUCCESS — todos los pasos marcados
    todos_completos = len(pasos_completados) == len(plan["pasos"])
    if todos_completos:
        st.success("Todos los pasos completados. Puedes continuar tu viaje.")

    # Métricas sensoriales de la ruta calculada
    render_metricas_entorno(
        afluencia=plan["afluencia_label"],
        ruido=plan["ruido_label"],
        retraso=plan["retraso_label"]
    )

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    # Botón a modo silencioso (solo si la ruta requiere taxi o comunicación)
    col1, col2 = st.columns(2)
    with col1:
        if st.button(LABEL_BOTON_SILENT):
            st.session_state.silent_mode = True
            st.rerun()
    with col2:
        if st.button(LABEL_BOTON_RESET):
            _resetear_viaje()
            st.toast(LABEL_TOAST_RESET)
            st.rerun()
