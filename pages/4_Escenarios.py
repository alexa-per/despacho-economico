import streamlit as st
from utils.state import get_sistema

sistema = get_sistema()
st.caption(f"📌 Sistema seleccionado: **{sistema}**")

st.title("Escenarios")
escenario = st.selectbox(
    "Selecciona un escenario (placeholder):",
    ["Base", "Fuel shock", "Outage", "Add storage", "Scarcity knob"],
    key="escenario"
)
st.write("Escenario seleccionado:", escenario)
