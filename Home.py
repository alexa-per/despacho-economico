import streamlit as st

st.set_page_config(page_title="Despacho Económico", layout="wide")

# ✅ Inicializar estado SOLO una vez
if "sistema" not in st.session_state:
    st.session_state["sistema"] = "SIN"

st.title("Simulador de despacho económico (México)")
st.write("Bienvenida/o 👋")

# ✅ Selector ligado a session_state
st.selectbox(
    "Selecciona el sistema eléctrico:",
    ["SIN", "BCA", "BCS"],
    key="sistema"
)

st.info(f"Sistema seleccionado: {st.session_state['sistema']}")

st.write("""
Esta app (en construcción) descargará demanda horaria real de CENACE
y correrá un despacho económico con optimización.
""")
