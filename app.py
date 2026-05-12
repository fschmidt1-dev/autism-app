"""
app.py — Entry point. Router entre páginas. No contiene lógica ni UI propia.
Inicializa session_state, aplica estilos globales y delega a la página activa.
"""

import streamlit as st
from config import APP_TITLE, APP_ICON
from ui._brand import aplicar_estilos_globales
from ui.home import render_home
from ui.panic import render_panic


def _inicializar_estado() -> None:
    """
    Garantiza que todas las claves de session_state existan antes de cualquier render.
    Protege contra resets de Streamlit en recarga móvil.
    """
    if "panic_mode" not in st.session_state:
        st.session_state.panic_mode = False
    if "plan_b" not in st.session_state:
        st.session_state.plan_b = None


def main() -> None:
    """
    Punto de entrada único. Configura la app, aplica estilos y enruta a la página correcta.
    """
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon=APP_ICON,
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    _inicializar_estado()
    aplicar_estilos_globales()

    if st.session_state.panic_mode:
        render_panic()
    else:
        render_home()


if __name__ == "__main__":
    main()
