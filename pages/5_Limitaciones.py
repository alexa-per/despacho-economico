def require_sistema() -> str:
    if "sistema" not in st.session_state:
        st.warning("Primero selecciona el sistema en la página **Home** (SIN/BCA/BCS).")
        st.stop()
    return st.session_state["sistema"]

import streamlit as st

def require_sistema() -> str:
    if "sistema" not in st.session_state:
        st.warning("Primero selecciona el sistema en la página **Home** (SIN/BCA/BCS).")
        st.stop()
    return st.session_state["sistema"]

sistema = require_sistema()
st.caption(f"📌 Sistema seleccionado en Home: **{sistema}**")

st.title("Limitaciones y supuestos")
st.markdown("""
**Qué sí modela (alcance mínimo):**
- Cada sistema (SIN/BCA/BCS) como bus aislado (sin transmisión interna).
- Demanda horaria + despacho por optimización.

**Qué NO modela (a propósito):**
- No modela red/transmisión ni congestión.
- No incluye unit commitment, reservas completas o N-1.
""")
