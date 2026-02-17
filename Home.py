import streamlit as st
from utils.state import sistema_sidebar

st.set_page_config(page_title="Despacho Económico", layout="wide")

sistema = sistema_sidebar()

st.title("Simulador de despacho económico (México)")
st.info(f"Sistema seleccionado: {sistema}")

st.write("""
Usa el menú de la izquierda para navegar por módulos.
""")
