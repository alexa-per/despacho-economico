import streamlit as st

st.set_page_config(page_title="Despacho Económico", layout="wide")

# Inicializa SOLO una vez
if "sistema" not in st.session_state:
    st.session_state["sistema"] = "SIN"

st.title("Simulador de despacho económico (México)")
st.write("Bienvenida/o 👋")

st.selectbox(
    "Selecciona el sistema eléctrico:",
    ["SIN", "BCA", "BCS"],
    key="sistema",
)

st.info(f"Sistema seleccionado: {st.session_state['sistema']}")

st.write("""
Usa el menú de la izquierda para navegar:
- Demanda: descarga/validación (Semana 2)
- Capacidades: datos 2024 y caso 2026
- Despacho: optimización (PyPSA)
- Escenarios: presets
- Limitaciones: supuestos y alcance
""")
