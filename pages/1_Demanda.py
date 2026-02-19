import streamlit as st
from utils.state import get_sistema

sistema = get_sistema()
st.caption(f"📌 Sistema seleccionado: **{sistema}**")

st.title("Demanda (CENACE)")
st.write("Aquí irá la descarga y validación de demanda horaria real.")

col1, col2 = st.columns(2)
with col1:
    st.date_input("Fecha inicio", key="fecha_inicio")
with col2:
    st.date_input("Fecha fin", key="fecha_fin")

st.button("Descargar demanda (próximamente)")
