import streamlit as st

st.set_page_config(page_title="Despacho Económico", layout="wide")
st.title("Simulador de despacho económico (México)")

# Inicializa SOLO una vez
if "sistema" not in st.session_state:
    st.session_state.sistema = "SIN"

st.selectbox(
    "Selecciona el sistema eléctrico:",
    ["SIN", "BCA", "BCS"],
    index=["SIN", "BCA", "BCS"].index(st.session_state.sistema),
    key="sistema",
)

st.write("DEBUG → sistema en session_state:", st.session_state.sistema)
