import streamlit as st
from utils.state import get_sistema

sistema = get_sistema()
st.caption(f"📌 Sistema seleccionado: **{sistema}**")

st.title("Capacidades")
st.write("Aquí definiremos capacidades por tecnología (2024) y el caso 2026.")
