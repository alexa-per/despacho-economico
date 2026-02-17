import streamlit as st

st.set_page_config(page_title="Despacho Económico", layout="wide")
st.title("Simulador de despacho económico (México)")

# 1) Inicializa una sola vez
if "sistema" not in st.session_state:
    st.session_state["sistema"] = "SIN"

# 2) Selectbox ligado al estado
st.selectbox(
    "Selecciona el sistema eléctrico:",
    ["SIN", "BCA", "BCS"],
    key="sistema",
)

st.info(f"Sistema seleccionado: {st.session_state['sistema']}")
