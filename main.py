from src.clean_cirugias import clean_cirugias
from src.clean_desmontaje import clean_desmontaje
from src.merge import merge_dataframes

if __name__ == "__main__":
    print("🧼 Ejecutando limpieza de cirugías...")
    clean_cirugias()

    print("🧼 Ejecutando limpieza de desmontaje...")
    clean_desmontaje()

    print("🔗 Ejecutando merge final...")
    merge_dataframes()

    print("✅ Proceso completo finalizado.")
