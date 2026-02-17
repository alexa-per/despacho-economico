import streamlit as st

st.set_page_config(page_title="Despacho Económico", layout="wide")

st.title("Simulador de despacho económico (México)")
st.write("""
Bienvenida/o 👋  
Esta app (en construcción) descargará demanda horaria real de CENACE para SIN/BCA/BCS
y correrá un despacho económico con optimización.

Usa el menú de la izquierda para navegar por módulos.
""")

st.info("Semana 1: Skeleton + documentación mínima. Próximo: demanda CENACE (Semana 2).")
