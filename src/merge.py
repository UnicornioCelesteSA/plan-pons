# src/merge.py

import pandas as pd
import os

def merge_dataframes():
    print("🔗 Ejecutando merge final...")

    # Cargar dataframes limpios
    df_cirugias = pd.read_parquet("data/df_cirugias_clean.parquet")
    df_desmontaje = pd.read_parquet("data/df_desmontaje_clean.parquet")

    # Asegurar que 'codigo_cirugia' esté en formato entero compatible
    df_cirugias["codigo_cirugia"] = pd.to_numeric(df_cirugias["codigo_cirugia"], errors="coerce").astype("Int64")
    df_desmontaje["codigo_cirugia"] = pd.to_numeric(df_desmontaje["codigo_cirugia"], errors="coerce").astype("Int64")

    # Hacer merge por 'codigo_cirugia'
    df_merged = pd.merge(df_cirugias, df_desmontaje, on="codigo_cirugia", how="outer", suffixes=("_cirugia", "_desmontaje"))

    # Crear columna estado_registro
    def clasificar(row):
        if pd.notnull(row["cliente"]) and pd.notnull(row["producto"]):
            return "completo"
        elif pd.notnull(row["cliente"]) and pd.isnull(row["producto"]):
            return "solo_cirugia"
        elif pd.isnull(row["cliente"]) and pd.notnull(row["producto"]):
            return "solo_desmontaje"
        else:
            return "sin_info"

    df_merged["estado_registro"] = df_merged.apply(clasificar, axis=1)

    # Crear carpeta output si no existe
    os.makedirs("output", exist_ok=True)

    # Guardar en carpeta output
    df_merged.to_parquet("output/merged_output.parquet", index=False)
    df_merged.to_excel("output/merged_output.xlsx", index=False)

    print("✅ Merge completado y archivos generados:")
    print("   - output/merged_output.parquet")
    print("   - output/merged_output.xlsx")
