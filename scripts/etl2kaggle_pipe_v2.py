import pandas as pd
import os
import shutil
import kagglehub

def extract():
    print("Iniciando extracción desde Kaggle...")
    os.makedirs('data/raw', exist_ok=True)
    
    # kagglehub 
    path = kagglehub.dataset_download("sudhanvahavekar/crop-yield-prediction-dataset")
    
    # copiamos el dataset a data/raw
    archivo_origen = os.path.join(path, "yield_df.csv")
    archivo_destino = "data/raw/yield_df.csv"
    shutil.copy(archivo_origen, archivo_destino)
    
    print("Extracción completada.")

def transform():
    print("Iniciando transformación...")
    os.makedirs('data/processed', exist_ok=True)
    
    df = pd.read_csv('data/raw/yield_df.csv')
    
    # columnas
    df = df.rename(columns={'Item': 'nombre_cultivo', 'hg/ha_yield': 'rendimiento'})
    
    # Limpiez
    df_clean = df.dropna()
    resumen = df_clean.groupby('nombre_cultivo')['rendimiento'].mean().reset_index()
    
    resumen.to_parquet('data/processed/resumen_cultivos.parquet')
    print("Transformación completada y guardada en Parquet.")

if __name__ == "__main__":
    extract()
    transform()