import pandas as pd
import os
import subprocess

def extract():
    print("Iniciando extracción desde Kaggle...")
    os.makedirs('data/raw', exist_ok=True)  
 
    dataset_name = "sudhanvahavekar/crop-yield-prediction-dataset" 
    subprocess.run(["kaggle", "datasets", "download", "-d", dataset_name, "-p", "data/raw", "--unzip"])
    print("Extracción completada.")

def transform():
    print("Iniciando transformación...")
    os.makedirs('data/processed', exist_ok=True)
    
    df = pd.read_csv('data/raw/yield_df.csv')
    #columnas
    df = df.rename(columns={'Item': 'nombre_cultivo', 'hg/ha_yield': 'rendimiento'})
    
    # agregacion
    df_clean = df.dropna()
    resumen = df_clean.groupby('nombre_cultivo')['rendimiento'].mean().reset_index()
    
    resumen.to_parquet('data/processed/resumen_cultivos.parquet')
    print("Transformación completada y guardada en Parquet.")

if __name__ == "__main__":
    extract()
    transform()