"""
silent_card.py — Pantalla silenciosa de comunicación con conductor.
Texto gigante sobre fondo negro. Sin interacciones salvo el botón de vuelta.
"""

import streamlit as st
from config import SILENT_CARD_TEXTO, LABEL_BOTON_VOLVER


def render_silent_card() -> None:
    """
    Renderiza la tarjeta de comunicación silenciosa a pantalla casi completa.
    El usuario muestra esta pantalla al conductor sin necesidad de hablar.
    """
    st.markdown(
        f"""<div class="silent-card-container">
            <p class="silent-card-label">Muestra esta pantalla al conductor</p>
            <p class="silent-card-text">{SILENT_CARD_TEXTO}</p>
        </div>""",
        unsafe_allow_html=True
    )

    st.write("")

    if st.button(LABEL_BOTON_VOLVER):
        st.session_state.silent_mode = False
        st.rerun()
