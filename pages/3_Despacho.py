import streamlit as st

def get_sistema_from_home() -> str:
    if "sistema" not in st.session_state:
        st.warning("Primero selecciona el sistema en la página **Home** (SIN/BCA/BCS).")
        st.stop()
    return st.session_state["sistema"]

sistema = get_sistema_from_home()
st.caption(f"📌 Sistema seleccionado en Home: **{sistema}**")

st.title("Despacho económico")
st.write("Aquí correremos la optimización y mostraremos despacho, costo total y precio marginal.")
st.write("Sistema activo para esta página:", sistema)

st.button("Correr despacho (próximamente)")
