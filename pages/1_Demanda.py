import streamlit as st
import pandas as pd
from utils.state import get_sistema
from utils.demanda import mock_demanda

st.title("Demanda (CENACE)")

sistema = get_sistema()
st.caption(f"📌 Sistema seleccionado: **{sistema}**")

col1, col2 = st.columns(2)
with col1:
    start = st.date_input("Fecha inicio", value=pd.to_datetime("2024-01-01"))
with col2:
    end = st.date_input("Fecha fin", value=pd.to_datetime("2024-01-03"))

if start > end:
    st.error("La fecha inicio no puede ser mayor que la fecha fin.")
    st.stop()

@st.cache_data(show_spinner=True)
def get_demanda_cached(sistema: str, start_str: str, end_str: str) -> pd.DataFrame:
    # Por ahora mock; en Semana 2 real lo cambiamos por fetch_cenace()
    return mock_demanda(sistema, start_str, end_str)

if st.button("Cargar demanda"):
    df = get_demanda_cached(sistema, start.isoformat(), end.isoformat())

    st.subheader("Vista previa")
    st.dataframe(df.head(20), use_container_width=True)

    st.subheader("Validaciones rápidas")
    # 1) duplicados por timestamp
    dup = df["timestamp"].duplicated().sum()
    st.write("Duplicados:", dup)

    # 2) faltantes en la secuencia horaria
    idx = pd.date_range(df["timestamp"].min(), df["timestamp"].max(), freq="H")
    missing = len(idx) - df["timestamp"].nunique()
    st.write("Horas faltantes (aprox):", missing)

    # 3) stats básicos
    st.write("Min MW:", float(df["demanda_mw"].min()))
    st.write("Max MW:", float(df["demanda_mw"].max()))
    st.write("Promedio MW:", float(df["demanda_mw"].mean()))

    st.subheader("Gráfico")
    st.line_chart(df.set_index("timestamp")["demanda_mw"])
