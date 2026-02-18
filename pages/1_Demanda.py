import streamlit as st

st.title("Demanda")

if "sistema" not in st.session_state:
    st.warning("Primero selecciona el sistema en la página Home.")
    st.stop()

st.write("Sistema activo:", st.session_state["sistema"])
