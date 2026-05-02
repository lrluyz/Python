import os
import pandas as pd

def eliminar_archivo(ruta):
    if os.path.exists(ruta):
        os.remove(ruta)
        print(f"Archivo eliminado: {ruta}")


def leer_excel(ruta_excel):
    df = pd.read_excel(ruta_excel)
    print(f"Excel leído: {ruta_excel} ({len(df)} filas, {len(df.columns)} columnas)")
    return df


def guardar_csv(df, ruta_csv):
    df.to_csv(ruta_csv, index=False, encoding="utf-8")
    print(f"CSV creado: {ruta_csv}")

if __name__ == "__main__":
    RUTA_EXCEL = "datos.xlsx"
    RUTA_CSV   = "datos.csv"

    if os.path.exists(RUTA_EXCEL):
        eliminar_archivo(RUTA_CSV)

        df = leer_excel(RUTA_EXCEL)
        guardar_csv(df, RUTA_CSV)
        
        eliminar_archivo(RUTA_EXCEL)

        print("Proceso completado.")

    else:
        print(f"El archivo {RUTA_EXCEL} no existe en la ruta");