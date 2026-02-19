import streamlit as st
from utils.state import get_sistema

sistema = get_sistema()
st.caption(f"📌 Sistema seleccionado: **{sistema}**")

st.title("Limitaciones y supuestos")
st.markdown("""
**Qué sí modela (alcance mínimo):**
- Cada sistema como bus aislado.
- Demanda horaria + despacho por optimización.

**Qué NO modela (a propósito):**
- No modela transmisión/congestión.
- No incluye unit commitment, reservas completas o N-1.
""")
