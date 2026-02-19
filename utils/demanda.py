import pandas as pd
import numpy as np
from datetime import datetime, timedelta, timezone

def mock_demanda(sistema: str, start: str, end: str) -> pd.DataFrame:
    """
    Genera demanda horaria falsa para probar UI + validaciones.
    start/end en formato 'YYYY-MM-DD'.
    """
    start_dt = pd.to_datetime(start)
    end_dt = pd.to_datetime(end) + pd.Timedelta(days=1)  # incluir el día final
    idx = pd.date_range(start_dt, end_dt, freq="H", inclusive="left")

    # señal simple: base + ciclo diario + ruido
    base = {"SIN": 35000, "BCA": 2500, "BCS": 700}.get(sistema, 1000)
    horas = np.arange(len(idx))
    daily = 0.15 * base * np.sin(2 * np.pi * (horas % 24) / 24)
    noise = np.random.normal(0, 0.03 * base, size=len(idx))

    df = pd.DataFrame({
        "timestamp": idx,
        "demanda_mw": (base + daily + noise).clip(lower=0),
        "sistema": sistema
    })
    return df
