import pandas as pd
from sqlalchemy import create_engine

# Config do banco
USER = "admin"
PASSWORD = "admin"
HOST = "localhost"
PORT = "5432"
DB = "ecommerce"

# Conexão com Postgres
engine = create_engine(f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}")

# Leitura de CSV (substitua pelo dataset baixado do Kaggle)
df = pd.read_csv("data/olist_orders_dataset.csv")

# Carrega para schema raw
df.to_sql("orders", engine, schema="raw", if_exists="append", index=False)

print("Ingestão concluída 🚀")
