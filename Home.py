import streamlit as st
from utils.state import get_sistema

st.set_page_config(page_title="Home", layout="wide")

st.title("Simulador de despacho económico (México)")
st.write("Bienvenida/o 👋")

# Selector principal en Home
st.session_state["sistema"] = st.selectbox(
    "Selecciona el sistema eléctrico:",
    ["SIN", "BCA", "BCS"],
    index=["SIN", "BCA", "BCS"].index(st.session_state.get("sistema", "SIN")),
    key="sistema_home",
)

st.info(f"Sistema seleccionado: {get_sistema()}")

st.write("""
Usa el menú de la izquierda para navegar por módulos.
""")
