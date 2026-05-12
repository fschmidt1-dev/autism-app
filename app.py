"""
app.py — Entry point. Router de 3 estados: home / panic / silent_card.
No contiene lógica ni UI propia. Inicializa estado y delega.
"""

import streamlit as st
from config import APP_TITLE, APP_ICON
from ui._brand import aplicar_estilos_globales
from ui.home import render_home
from ui.panic import render_panic
from ui.silent_card import render_silent_card


def _inicializar_estado() -> None:
    """
    Garantiza que todas las claves de session_state existan antes de cualquier render.
    Protege contra el reset de Streamlit en recarga móvil.
    """
    claves_default = {
        "panic_mode": False,
        "plan_b": None,
        "silent_mode": False,
        "pasos_completados": []
    }
    for clave, valor in claves_default.items():
        if clave not in st.session_state:
            st.session_state[clave] = valor


def main() -> None:
    """
    Punto de entrada único. Configura, aplica estilos y enruta a la página correcta.
    """
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon=APP_ICON,
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    _inicializar_estado()
    aplicar_estilos_globales()

    # Router de 3 estados — orden importa: silent > panic > home
    if st.session_state.silent_mode:
        render_silent_card()
    elif st.session_state.panic_mode:
        render_panic()
    else:
        render_home()


if __name__ == "__main__":
    main()
