import streamlit as st

st.set_page_config(page_title="Despacho Económico", layout="wide")

st.title("Simulador de despacho económico (México)")

st.write("Bienvenida/o 👋")

# 🔹 Selector de sistema
sistema = st.selectbox(
    "Selecciona el sistema eléctrico:",
    ["SIN", "BCA", "BCS"]
)

# 🔹 Guardamos selección
st.session_state["sistema"] = sistema

st.info(f"Sistema seleccionado: {sistema}")

st.write("""
Esta app (en construcción) descargará demanda horaria real de CENACE
y correrá un despacho económico con optimización.
""")
