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

st.title("Escenarios")
st.write("Aquí estarán los 5 escenarios preset (base, fuel shock, outage, etc.).")

escenario = st.selectbox(
    "Selecciona un escenario (placeholder):",
    ["Base", "Fuel shock", "Outage", "Add storage", "Scarcity knob"],
    key="escenario"
)
st.write("Escenario seleccionado:", escenario)
