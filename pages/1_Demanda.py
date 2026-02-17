import streamlit as st

st.title("Demanda")

sistema = st.session_state.get("sistema", "SIN")
st.write(f"Sistema activo: {sistema}")

st.write("Aquí irá la descarga de demanda horaria de CENACE.")
