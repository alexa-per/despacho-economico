import pandas as pd
import numpy as np

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
