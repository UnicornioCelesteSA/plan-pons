# src/clean_desmontaje.py

import pandas as pd

def clean_desmontaje():
    # Cargar archivo original
    df = pd.read_excel("data/df_desmontaje.xlsx")

    # Normalizar nombres de columnas
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Asegurar que 'mes_ano' esté presente
    if "mes_ano" not in df.columns:
        raise ValueError("La columna 'mes_ano' no existe en df_desmontaje.xlsx")

    # (Opcional) Si más adelante queremos calcular fechas reales
    # df["fecha_desmontaje"] = pd.to_datetime(df["mes_ano"], format="%Y-%m", errors="coerce")

    # Guardar archivo limpio
    df.to_parquet("data/df_desmontaje_clean.parquet", index=False)

    print("✅ df_desmontaje_clean.parquet generado correctamente.")
