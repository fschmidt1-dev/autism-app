def render_encabezado_sistema() -> None:
    """Renderiza el logo y el subtítulo del sistema en la parte superior."""
    logo_svg = """
    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
        <svg viewBox="0 0 400 400" width="36" height="36" xmlns="http://www.w3.org/2000/svg">
            <g transform="translate(130, 100)">
                <rect x="0" y="0" width="40" height="200" rx="6" fill="#528DAB"/>
                <rect x="100" y="0" width="40" height="200" rx="6" fill="#528DAB"/>
                <circle cx="70" cy="100" r="26" fill="#87C39A"/>
            </g>
        </svg>
        <span style="font-family: 'Instrument Sans', sans-serif; font-size: 28px; font-weight: 700; color: #0A1F44; letter-spacing: -0.02em;">Navify</span>
    </div>
    """
    st.markdown(logo_svg, unsafe_allow_html=True)
    st.markdown(f"<p class='system-subtitle' style='color: #3F4F63; font-size: 13px; letter-spacing: 2px; text-transform: uppercase; margin-top: 0;'>SISTEMA DE RUTEO TÁCTICO</p>", unsafe_allow_html=True)
