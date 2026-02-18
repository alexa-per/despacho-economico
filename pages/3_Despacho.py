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

st.title("Despacho económico")
st.write("Aquí correremos la optimización (PyPSA) y mostraremos resultados.")
st.button("Correr despacho (próximamente)")
