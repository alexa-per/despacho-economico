import streamlit as st
from utils.state import get_sistema

sistema = get_sistema()
st.caption(f"📌 Sistema seleccionado: **{sistema}**")

st.title("Despacho económico")
st.write("Aquí correremos la optimización (PyPSA) y mostraremos resultados.")
st.button("Correr despacho (próximamente)")
