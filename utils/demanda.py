import pandas as pd
import numpy as np

#Esta funcion es la que da datos falsos tener cuidado de no mantenerla al final!!!
def mock_demanda(sistema: str, start: str, end: str) -> pd.DataFrame:
    start_dt = pd.to_datetime(start)
    end_dt = pd.to_datetime(end) + pd.Timedelta(days=1)  # incluir día final
    idx = pd.date_range(start_dt, end_dt, freq="H", inclusive="left")

    base = {"SIN": 35000, "BCA": 2500, "BCS": 700}.get(sistema, 1000)
    horas = np.arange(len(idx))
    daily = 0.15 * base * np.sin(2 * np.pi * (horas % 24) / 24)
    noise = np.random.normal(0, 0.03 * base, size=len(idx))

    demanda = np.clip(base + daily + noise, a_min=0, a_max=None)

    df = pd.DataFrame({
        "timestamp": idx,
        "demanda_mw": demanda,
        "sistema": sistema
    })
    return df

# utils/demanda.py
from __future__ import annotations

import datetime as dt
import pandas as pd

from utils.cenace_client import fetch_caezc_mda


def demanda_cenace(sistema: str, start_str: str, end_str: str) -> pd.DataFrame:
    start = dt.date.fromisoformat(start_str)
    end = dt.date.fromisoformat(end_str)

    df_zonas = fetch_caezc_mda(sistema=sistema, start=start, end=end, zonas=None)

    # Agregamos todas las zonas para tener una sola curva
    df = (
        df_zonas.groupby("timestamp", as_index=False)["demanda_mw"]
        .sum()
        .sort_values("timestamp")
    )
    return df
