import streamlit as st

def get_sistema_from_home() -> str:
    if "sistema" not in st.session_state:
        st.warning("Primero selecciona el sistema en la página **Home** (SIN/BCA/BCS).")
        st.stop()
    return st.session_state["sistema"]

sistema = get_sistema_from_home()
st.caption(f"📌 Sistema seleccionado en Home: **{sistema}**")

st.title("Capacidades")
st.write("Aquí definiremos capacidades por tecnología (2024) y el caso 2026.")
st.write("Sistema activo para esta página:", sistema)

st.info("Tip: más adelante leeremos capacidades desde CSV para que sea auditable.")
