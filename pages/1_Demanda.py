import streamlit as st
import pandas as pd
from utils.state import get_sistema
from utils.demanda import mock_demanda

st.title("Demanda (CENACE)")

# ✅ Guardaremos aquí el último df cargado para no perderlo entre clicks/páginas
if "df_demanda" not in st.session_state:
    st.session_state["df_demanda"] = None

# (Opcional pero recomendado) guardar también con qué fechas se generó el df
if "demanda_meta" not in st.session_state:
    st.session_state["demanda_meta"] = None

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
    return mock_demanda(sistema, start_str, end_str)

# ✅ Botón para cargar demanda
if st.button("Cargar demanda"):
    df = get_demanda_cached(sistema, start.isoformat(), end.isoformat())
    st.session_state["df_demanda"] = df
    st.session_state["demanda_meta"] = {
        "sistema": sistema,
        "start": start.isoformat(),
        "end": end.isoformat(),
    }

# ✅ A PARTIR DE AQUÍ: mostrar resultados si ya hay un df cargado
df = st.session_state.get("df_demanda")
meta = st.session_state.get("demanda_meta")

if df is not None:
    st.divider()
    st.subheader("Resumen")

    # KPIs
    pico = float(df["demanda_mw"].max())
    prom = float(df["demanda_mw"].mean())
    energia_mwh = float(df["demanda_mw"].sum())  # MW * 1h = MWh

    c1, c2, c3 = st.columns(3)
    c1.metric("Pico (MW)", f"{pico:,.0f}")
    c2.metric("Promedio (MW)", f"{prom:,.0f}")
    c3.metric("Energía total (MWh)", f"{energia_mwh:,.0f}")

    st.subheader("Vista previa")
    st.dataframe(df.head(30), use_container_width=True)

    st.subheader("Validaciones rápidas")
    dup = int(df["timestamp"].duplicated().sum())
    st.write("Duplicados:", dup)

    idx = pd.date_range(df["timestamp"].min(), df["timestamp"].max(), freq="H")
    missing = int(len(idx) - df["timestamp"].nunique())
    st.write("Horas faltantes (aprox):", missing)

    st.write("Min MW:", float(df["demanda_mw"].min()))
    st.write("Max MW:", float(df["demanda_mw"].max()))
    st.write("Promedio MW:", float(df["demanda_mw"].mean()))

    st.subheader("Gráfico")
    st.line_chart(df.set_index("timestamp")["demanda_mw"])

    # ✅ Descarga CSV (ya no depende de estar dentro del botón)
    csv = df.to_csv(index=False).encode("utf-8")

    # Usar el nombre con el rango real con que se generó (si existe meta)
    if meta is not None:
        fname = f"demanda_{meta['sistema']}_{meta['start']}_{meta['end']}.csv"
    else:
        fname = f"demanda_{sistema}_{start.isoformat()}_{end.isoformat()}.csv"

    st.download_button(
        "⬇️ Descargar CSV",
        data=csv,
        file_name=fname,
        mime="text/csv",
    )

    # ✅ Botón para limpiar
    if st.button("🧹 Limpiar demanda cargada"):
        st.session_state["df_demanda"] = None
        st.session_state["demanda_meta"] = None
        st.rerun()
else:
    st.info("Presiona **Cargar demanda** para generar y visualizar la demanda.")
