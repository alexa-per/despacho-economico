def require_sistema() -> str:
    if "sistema" not in st.session_state:
        st.warning("Primero selecciona el sistema en la página **Home** (SIN/BCA/BCS).")
        st.stop()
    return st.session_state["sistema"]

import streamlit as st

def require_sistema() -> str:
    if "sistema" not in st.session_state:
        st.warning("Primero selecciona el sistema en la página **Home** (SIN/BCA/BCS).")
        st.stop()
    return st.session_state["sistema"]

sistema = require_sistema()
st.caption(f"📌 Sistema seleccionado en Home: **{sistema}**")

st.title("Capacidades")
st.write("Aquí definiremos capacidades por tecnología (2024) y el caso 2026.")
st.info("Más adelante leeremos capacidades desde CSV para que sea auditable.")
