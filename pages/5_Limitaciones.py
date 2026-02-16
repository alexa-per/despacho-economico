import streamlit as st

st.title("Limitaciones y supuestos")
st.markdown("""
**Qué sí modela (por ahora):**
- App por sistema (SIN/BCA/BCS) como bus aislado.
- Demanda horaria y despacho por optimización.

**Qué NO modela (a propósito):**
- No modela red/transmisión ni congestión.
- No incluye unit commitment, reservas completas o N-1.
""")
