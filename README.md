# Data Engineering E-commerce Project

Este projeto é um estudo em **Engenharia de Dados**, utilizando dados públicos de e-commerce (Kaggle Olist Dataset).
O objetivo foi construir uma **plataforma de dados** completa, passando por ingestão, modelagem, pipelines e análises, utilizando **Postgres, Python, Azure e PySpark**.

---

## 🚀 Objetivos do Projeto

* Praticar **ETL/ELT** com grandes volumes de dados.
* Trabalhar com **SQL avançado** e **Postgres**.
* Desenvolver pipelines em **Python**.
* Versionar código com **Git/GitHub**.
* Evoluir para integração com **Azure (Data Factory, Databricks, Synapse)**.
* Construir um **Lakehouse** com PySpark.

---

## 📂 Estrutura de Pastas

```
data-engineering-ecommerce/
│── data/               # Datasets brutos (CSV do Kaggle)
│── docs/               # Documentação (diagramas, anotações)
│── src/                # Script Python de ingestão unificado
│   └── ingest_data.py
│── docker/             # Configuração do Docker (docker-compose.yml)
│── requirements.txt    # Dependências do projeto
│── README.md           # Documentação do projeto
```

---

## 🐳 Etapa 1 – Configuração do Banco de Dados (Postgres)

O Postgres foi configurado dentro da pasta `docker/` utilizando Docker Compose:

```bash
docker-compose up -d
```

É possível verificar se o container está rodando com:

```bash
docker ps
```

Acesso ao banco foi realizado com:

```bash
docker exec -it postgres psql -U admin -d ecommerce
```

O schema e as tabelas iniciais foram criados da seguinte forma:

```sql
-- Schema
CREATE SCHEMA IF NOT EXISTS raw;

-- Orders
CREATE TABLE IF NOT EXISTS raw.orders (
    order_id VARCHAR PRIMARY KEY,
    customer_id VARCHAR,
    order_status VARCHAR,
    order_purchase_timestamp TIMESTAMP,
    order_approved_at TIMESTAMP,
    order_delivered_carrier_date TIMESTAMP,
    order_delivered_customer_date TIMESTAMP,
    order_estimated_delivery_date TIMESTAMP
);

-- Customers
CREATE TABLE IF NOT EXISTS raw.customers (
    customer_id VARCHAR PRIMARY KEY,
    customer_unique_id VARCHAR,
    customer_zip_code_prefix VARCHAR,
    customer_city VARCHAR,
    customer_state VARCHAR
);

-- Order Items
CREATE TABLE IF NOT EXISTS raw.items (
    order_id VARCHAR,
    order_item_id INT,
    product_id VARCHAR,
    seller_id VARCHAR,
    shipping_limit_date TIMESTAMP,
    price NUMERIC,
    freight_value NUMERIC
);

-- Products
CREATE TABLE IF NOT EXISTS raw.products (
    product_id VARCHAR PRIMARY KEY,
    product_category_name VARCHAR,
    product_name_length INT,
    product_description_length INT,
    product_photos_qty INT,
    product_weight_g INT,
    product_length_cm INT,
    product_height_cm INT,
    product_width_cm INT
);

-- Payments
CREATE TABLE IF NOT EXISTS raw.payments (
    order_id VARCHAR,
    payment_sequential INT,
    payment_type VARCHAR,
    payment_installments INT,
    payment_value NUMERIC
);
```

---

## 🐍 Etapa 2 – Configuração do Ambiente Python

Foi criado um ambiente virtual para o projeto:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

As dependências foram instaladas com:

```bash
pip install pandas psycopg2 sqlalchemy
pip freeze > requirements.txt
```

---

## 📊 Etapa 3 – Ingestão de Dados Unificada

Um único script Python (`src/ingest_data.py`) foi utilizado para realizar a ingestão de todos os CSVs simultaneamente:

```python
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
       
        # Leitura de CSV
        df = pd.read_csv(item, sep=",")
        df.columns = df.columns.str.strip().str.replace('"', '')

        print(f"Colunas lidas: {df.columns.tolist()}")
        # Carregamento para schema raw
        df.to_sql(target_table, engine, schema="raw", if_exists="append", index=False)
    else:
        print("Categoria não encontrada")

print("Ingestão concluída 🚀")
```

---

## 📝 Etapa 4 – Diagrama ER

O diagrama ER foi criado utilizando [dbdiagram.io](https://dbdiagram.io).
Exemplo de relacionamento básico:

```sql
Table orders {
  order_id varchar [pk]
  customer_id varchar
}

Table customers {
  customer_id varchar [pk]
  customer_city varchar
  customer_state varchar
}

Ref: orders.customer_id > customers.customer_id
```

O diagrama exportado foi salvo em `docs/er_diagram.png`.

---

## 🔍 Etapa 5 – Consultas Exploratorias

Alguns exemplos de queries SQL executadas durante o projeto:

```sql
-- Total de pedidos por status
SELECT order_status, COUNT(*) 
FROM raw.orders 
GROUP BY order_status;

-- Ticket médio por cliente
SELECT c.customer_unique_id, AVG(p.payment_value) as avg_ticket
FROM raw.customers c
JOIN raw.orders o ON c.customer_id = o.customer_id
JOIN raw.payments p ON o.order_id = p.order_id
GROUP BY c.customer_unique_id
ORDER BY avg_ticket DESC
LIMIT 10;
```

## 🔮 Próximos Passos

* Criação de pipelines incrementais para ingestão.
* Transformações e modelagem para camada **curated**.
* Integração com **Azure Data Factory, Databricks e Synapse**.
* Construção de **Lakehouse com PySpark**.
* Desenvolvimento de dashboards ou análises exploratórias.

---

📌 *Este projeto será publicado passo a passo no LinkedIn como portfólio de Engenharia de Dados.*
