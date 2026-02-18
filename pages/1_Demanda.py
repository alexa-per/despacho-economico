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

st.title("Demanda (CENACE)")
st.write("Aquí irá la descarga y validación de demanda horaria real.")

col1, col2 = st.columns(2)
with col1:
    st.date_input("Fecha inicio", key="fecha_inicio")
with col2:
    st.date_input("Fecha fin", key="fecha_fin")

st.button("Descargar demanda (próximamente)")
