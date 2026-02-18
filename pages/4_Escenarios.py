import streamlit as st

def get_sistema_from_home() -> str:
    if "sistema" not in st.session_state:
        st.warning("Primero selecciona el sistema en la página **Home** (SIN/BCA/BCS).")
        st.stop()
    return st.session_state["sistema"]

sistema = get_sistema_from_home()
st.caption(f"📌 Sistema seleccionado en Home: **{sistema}**")

st.title("Escenarios")
st.write("Aquí estarán los 5 escenarios preset (fuel shock, outage, storage, etc.).")
st.write("Sistema activo para esta página:", sistema)

escenario = st.selectbox(
    "Selecciona un escenario (placeholder):",
    ["Base", "Fuel shock", "Outage", "Add storage", "Scarcity knob"]
)
st.write("Escenario seleccionado:", escenario)
