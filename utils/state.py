import streamlit as st

SYSTEMS = ["SIN", "BCA", "BCS"]

def sistema_sidebar() -> str:
    """Muestra selector en el sidebar y regresa el sistema seleccionado."""
    if "sistema" not in st.session_state:
        st.session_state["sistema"] = "SIN"

    st.sidebar.selectbox(
        "Sistema eléctrico",
        SYSTEMS,
        key="sistema",
    )

    return st.session_state["sistema"]
