import pandas as pd
import os
from sqlalchemy import create_engine
from pathlib import Path

# Config do banco
USER = "admin"
PASSWORD = "admin"
HOST = "localhost"
PORT = "5432"
DB = "ecommerce"
PATH = os.path.join(Path(__file__).resolve().parent.parent,"data")

list_category:list = ["orders","customers", "items", "products", "payments" ]
# Conexão com Postgres
engine = create_engine(f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}")

csv_files = [os.path.join( PATH, file) for file in os.listdir( PATH) if file.endswith(".csv")]

for item in csv_files:

    filename = os.path.basename(item).lower()

    target_table = None
    for category in list_category:
        if category in item:
            target_table = category
            break
    
    if target_table:
   
        # Leitura de CSV (substitua pelo dataset baixado do Kaggle)
        df = pd.read_csv(item,sep=",")

        df.columns = df.columns.str.strip().str.replace('"', '')

        print(f"Colunas lidas: {df.columns.tolist()}")
        # Carrega para schema raw
        df.to_sql(target_table, engine, schema="raw", if_exists="append", index=False)
    else:
        print("Categoria não encontrada")

print("Ingestão concluída 🚀")


