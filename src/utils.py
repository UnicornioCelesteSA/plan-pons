def imprimir_resumen(df):
    print("Total registros:", len(df))
    print(df["estado_registro"].value_counts(dropna=False))
