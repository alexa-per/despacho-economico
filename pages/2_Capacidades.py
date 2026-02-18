import streamlit as st

st.title("Capacidad")

if "sistema" not in st.session_state:
    st.warning("Primero selecciona el sistema en la página Home.")
    st.stop()

st.write("Sistema activo:", st.session_state["sistema"])

st.title("Capacidades")
st.write("Aquí definiremos capacidades por tecnología y casos 2024/2026.")
