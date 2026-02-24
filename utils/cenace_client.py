# utils/cenace_client.py
from __future__ import annotations

import datetime as dt
from typing import Any, Dict, List, Optional

import pandas as pd
import requests

# SW-CAEZC (SIM) usa REST GET y se invoca con URL + parámetros en la ruta. :contentReference[oaicite:2]{index=2}
BASE_URL = "https://ws01.cenace.gob.mx:8082/SWCAEZC/SIM"


def _ymd(d: dt.date) -> tuple[str, str, str]:
    return (f"{d.year:04d}", f"{d.month:02d}", f"{d.day:02d}")


def fetch_caezc_mda(
    sistema: str,
    start: dt.date,
    end: dt.date,
    zonas: Optional[List[str]] = None,
    formato: str = "JSON",
    timeout_sec: int = 30,
) -> pd.DataFrame:
    """
    Descarga datos del SW-CAEZC (CENACE SIM) para proceso MDA (GET, REST).
    Manual: formato de invocación y parámetros en la URL. :contentReference[oaicite:3]{index=3}

    Devuelve DataFrame con columnas:
      - timestamp
      - zona_carga
      - demanda_mw (aprox; ver nota)

    Nota: El servicio está pensado para resultados de mercado; el campo suele venir como energía horaria.
    Para una hora, MWh es equivalente a MW promedio de esa hora.
    """
    sistema = sistema.upper().strip()
    if sistema not in {"SIN", "BCA", "BCS"}:
        raise ValueError("sistema debe ser SIN, BCA o BCS")

    if start > end:
        raise ValueError("start no puede ser mayor que end")

    # Muchos servicios del SIM limitan ventanas cortas (p.ej. 1–7 días en manuales). :contentReference[oaicite:4]{index=4}
    if (end - start).days > 6:
        raise ValueError("Rango máximo: 7 días (reduce el periodo).")

    y1, m1, d1 = _ymd(start)
    y2, m2, d2 = _ymd(end)

    parts = [BASE_URL, sistema, "MDA"]

    if zonas:
        # Manuales del SIM suelen pedir lista separada por comas en la URL. :contentReference[oaicite:5]{index=5}
        zonas_norm = [z.strip().upper().replace(" ", "-") for z in zonas]
        parts.append(",".join(zonas_norm))

    parts += [y1, m1, d1, y2, m2, d2, formato.upper()]
    url = "/".join(parts)

    # En algunos entornos, el SSL del puerto 8082 puede dar problemas.
    # Para clase/prototipo, verify=False suele evitar bloqueos en Streamlit Cloud.
    resp = requests.get(url, timeout=timeout_sec, verify=False)
    resp.raise_for_status()

    data: Any = resp.json()

    rows: List[Dict[str, Any]] = []

    def walk(obj: Any) -> None:
        if isinstance(obj, list):
            for it in obj:
                walk(it)
        elif isinstance(obj, dict):
            keys = set(obj.keys())
            needed = {"zona_carga", "fecha", "hora", "total_cargas"}
            if needed.issubset(keys):
                rows.append(
                    {
                        "zona_carga": obj.get("zona_carga"),
                        "fecha": obj.get("fecha"),
                        "hora": obj.get("hora"),
                        "valor": obj.get("total_cargas"),
                    }
                )
            for v in obj.values():
                walk(v)

    walk(data)

    if not rows:
        raise RuntimeError(
            "No pude extraer registros del JSON. "
            "Probablemente cambió la estructura de respuesta del servicio."
        )

    df = pd.DataFrame(rows)
    df["hora"] = pd.to_numeric(df["hora"], errors="coerce").astype("Int64")
    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")

    # timestamp = fecha + hora (hora de operación)
    df["timestamp"] = pd.to_datetime(df["fecha"]) + pd.to_timedelta(df["hora"].fillna(0), unit="h")

    # Interpretación práctica para la app: MW promedio por hora
    df["demanda_mw"] = df["valor"]

    return df[["timestamp", "zona_carga", "demanda_mw"]].sort_values(["timestamp", "zona_carga"])
