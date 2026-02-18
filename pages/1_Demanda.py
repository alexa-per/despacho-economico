import streamlit as st

def get_sistema_from_home() -> str:
    if "sistema" not in st.session_state:
        st.warning("Primero selecciona el sistema en la página **Home** (SIN/BCA/BCS).")
        st.stop()
    return st.session_state["sistema"]

sistema = get_sistema_from_home()
st.caption(f"📌 Sistema seleccionado en Home: **{sistema}**")

st.title("Demanda")
st.write("Aquí irá la descarga y validación de demanda horaria de CENACE.")
st.write("Sistema activo para esta página:", sistema)

# Placeholder UI (para que ya se vea el flujo)
col1, col2 = st.columns(2)
with col1:
    st.date_input("Fecha inicio", key="fecha_inicio")
with col2:
    st.date_input("Fecha fin", key="fecha_fin")

st.button("Descargar demanda (próximamente)")
