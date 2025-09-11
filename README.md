# Data Engineering E-commerce Project

Este projeto é um estudo em **Engenharia de Dados**, utilizando dados públicos de e-commerce (Kaggle Olist Dataset).
O objetivo foi construir uma **plataforma de dados** completa, passando por ingestão, modelagem, pipelines e análises, utilizando **Postgres, Python, Azure e PySpark**.

---

## 🚀 Objetivos do Projeto

* Praticar **ETL/ELT** com grandes volumes de dados.
* Trabalhar com **SQL avançado** e **Postgres**.
* Desenvolver pipelines em **Python**.
* Evoluir para integração com **Azure (Data Factory, Databricks, Synapse)**.
* Construir um **Lakehouse** com PySpark.

---

## 📂 Estrutura de Pastas

```
data-engineering-ecommerce/
│── data/               # Datasets brutos (CSV do Kaggle)
│── docs/               # Documentação, diagramas, consultas SQL
│   ├── diagrama_er.sql
│   └── consultas.sql
│── src/                # Scripts Python de ingestão
│   └── ingest.py
│── docker/             # Configuração do Docker
│   └── docker-compose.yml
│   └── table.sql       # Criação de schema e tabelas no Postgres
│── requirements.txt    # Dependências do projeto
│── README.md           # Documentação do projeto
```

---

## 🐳 Etapa 1 – Banco de Dados (Postgres)

O Postgres foi configurado usando Docker Compose (`docker/docker-compose.yml`).
O schema e as tabelas foram criados no arquivo `docker/table.sql`.

---

## 🐍 Etapa 2 – Ambiente Python

O projeto pode ser executado em um **ambiente virtual** para garantir dependências isoladas.

---

## 📊 Etapa 3 – Ingestão de Dados

A ingestão de todos os CSVs é realizada pelo script `src/ingest.py`.
Ele lê os arquivos de dados e carrega nas tabelas do schema `raw` no Postgres.

---

## 📝 Etapa 4 – Diagrama ER

O diagrama ER do projeto está disponível em `docs/diagrama_er.sql`.
O diagrama exportado foi salvo em `docs/er_diagram.png`.

---

## 🔍 Etapa 5 – Consultas Exploratorias

As consultas exploratórias utilizadas durante o projeto estão disponíveis em `docs/consultas.sql`.

---

## 🔮 Próximos Passos

* Criação de pipelines incrementais para ingestão.
* Transformações e modelagem para camada **curated**.
* Integração com **Azure Data Factory, Databricks e Synapse**.
* Construção de **Lakehouse com PySpark**.
* Desenvolvimento de dashboards ou análises exploratórias.

---

📌 *Este projeto será publicado passo a passo no LinkedIn como portfólio de Engenharia de Dados.*


