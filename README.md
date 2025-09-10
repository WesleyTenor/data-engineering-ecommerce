# Data Engineering E-commerce Project

Projeto de estudos em **Engenharia de Dados**, utilizando dados públicos de e-commerce (Kaggle Olist Dataset).  
O objetivo é construir uma **plataforma de dados** completa, passando por ingestão, modelagem, pipelines e análises, utilizando **Postgres, Python, Azure e PySpark**.

---

## 🚀 Objetivos do Projeto

- Praticar **ETL/ELT** com grandes volumes de dados.  
- Trabalhar com **SQL avançado** e **Postgres**.  
- Desenvolver pipelines em **Python**.  
- Versionar código com **Git/GitHub**.  
- Evoluir para integração com **Azure (Data Factory, Databricks, Synapse)**.  

---

## 📂 Estrutura de Pastas

data-engineering-ecommerce/
│── data/ # Datasets brutos (CSV do Kaggle)
│── docs/ # Documentação (diagramas, anotações)
│── src/ # Scripts Python
│ └── ingest.py # Script inicial de ingestão
│── docker/ # Configuração do Docker (Postgres)
│ └── docker-compose.yml
│── requirements.txt # Dependências do projeto
│── README.md # Documentação do projeto



---

## 🐳 Subindo o Postgres com Docker Compose

## Dentro da pasta `docker/`, execute:
```bash
docker-compose up -d

## Verificar se o container está rodando:
docker ps

## Acessar o Banco
docker exec -it postgres psql -U admin -d ecommerce

🐍 Configuração do Ambiente Python
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

Dependencias
pip install pandas psycopg2 sqlalchemy
pip freeze > requirements.txt



