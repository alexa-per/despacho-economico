import streamlit as st

SYSTEMS = ["SIN", "BCA", "BCS"]

def get_sistema() -> str:
    """
    Regresa el sistema seleccionado.
    Si aún no existe (por sesión nueva o porque entraron directo a una página),
    muestra un selector y lo guarda.
    """
    if "sistema" not in st.session_state:
        st.warning("No hay sistema seleccionado todavía. Elige uno para continuar:")
        st.session_state["sistema"] = st.selectbox(
            "Sistema eléctrico",
            SYSTEMS,
            key="sistema_selector_fallback",
        )
    return st.session_state["sistema"]
