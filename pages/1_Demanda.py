import streamlit as st
from utils.state import sistema_sidebar

sistema = sistema_sidebar()

st.title("Demanda")
st.write(f"Sistema activo: {sistema}")
st.write("Aquí irá la descarga de demanda horaria de CENACE.")
