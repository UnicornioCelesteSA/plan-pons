# src/clean_cirugias.py

import pandas as pd

def clean_cirugias():
    # Cargar el archivo original
    df = pd.read_excel("data/df_cirugias.xlsx")

    # Normalizar nombres de columnas
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Asegurar que 'codigo_cirugia' sea int para el merge posterior
    if "codigo_cirugia" in df.columns:
        df["codigo_cirugia"] = pd.to_numeric(df["codigo_cirugia"], errors="coerce").astype("Int64")

    # Asegurar que 'fecha_cirugia' sea datetime si existe
    if "fecha_cirugia" in df.columns:
        df["fecha_cirugia"] = pd.to_datetime(df["fecha_cirugia"], errors="coerce")

    # === ✅ Ajuste importante: mantener todos los estados posibles ===
    if "estado" in df.columns:
        df["estado"] = df["estado"].astype(str)

        estados_posibles = [
            "Facturada",
            "Cancelada",
            "Entregada",
            "Para Facturar",
            "Sin Costo",
            "Suspendida",
            ""  # incluir también vacíos para filtrado
        ]

        df["estado"] = pd.Categorical(df["estado"], categories=estados_posibles)

        print("🗂️ Columna 'estado' ajustada con categorías completas.")
    else:
        print("⚠️ Advertencia: no se encontró columna 'estado'.")

    # Guardar como Parquet
    df.to_parquet("data/df_cirugias_clean.parquet", index=False)
    print("✅ df_cirugias_clean.parquet generado correctamente.")
