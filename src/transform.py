from sqlalchemy import create_engine, text
import pandas as pd

list_tables:list = ["orders","customers", "items", "products", "payments" ]

class Transform:
    def __init__(self, user="admin", password="admin", host="localhost", port=5432, db="ecommerce"):
        self.engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")
        self._create_schema()

    def _create_schema(self):
        """Garante que o schema curated exista"""
        with self.engine.connect() as conn:
            conn.execute(text("CREATE SCHEMA IF NOT EXISTS curated"))
            conn.commit()

    def run(self):
        """Executa todas as transformações"""
        self.transform_orders()
        self.transform_customers()
        self.transform_items()
        self.transform_products()
        self.transform_payments()
        

    def transform_orders(self):
        df = pd.read_sql("SELECT * FROM raw.orders", self.engine)

        # Conversões de datas
        date_cols = [
            "order_purchase_timestamp",
            "order_approved_at",
            "order_delivered_carrier_date",
            "order_delivered_customer_date",
            "order_estimated_delivery_date"
        ]
        for col in date_cols:
            df[col] = pd.to_datetime(df[col], errors="coerce")

        df.drop_duplicates(inplace=True)

        self._save_to_curated(df, "orders")

    def transform_customers(self):
        df = pd.read_sql("SELECT * FROM raw.customers", self.engine)
        df["customer_zip_code_prefix"] = pd.to_numeric(df["customer_zip_code_prefix"], errors="coerce")

        self._save_to_curated(df, "customers")

    def transform_items(self):
        df = pd.read_sql("SELECT * FROM raw.items", self.engine)
         
        df["shipping_limit_date"] = pd.to_datetime(df["shipping_limit_date"])
       
        float_columns = ["price","freight_value"]
        for col in float_columns:
            df[col] = pd.to_numeric(df[col])

        self._save_to_curated(df, "items")

    def transform_products(self, df:pd.DataFrame):
        """"""
        df = pd.read_sql("SELECT * FROM raw.products", self.engine)
        int_columns = [
            "product_name_length",
            "product_description_length",
            "product_photos_qty",
            "product_weight_g",
            "product_length_cm",
            "product_height_cm",
            "product_width_cm"
        ]
        for col in int_columns:
            df[col] = pd.to_numeric(df[col])

        self._save_to_curated(df, "products")

    def transform_payments(self, df:pd.DataFrame):
        """"""
        df = pd.read_sql("SELECT * FROM raw.payments", self.engine)
        int_columns = [
            "payment_sequential",
            "payment_installments",
            "payment_value"
        ]
        for col in int_columns:
            df[col] = pd.to_numeric(df[col])

        self._save_to_curated(df,"payments")



    def _save_to_curated(self, df: pd.DataFrame, table_name: str):
        """Grava o DataFrame no schema curated"""
        if df.empty:
            print(f"[WARN] Tabela {table_name} está vazia, não foi gravada.")
            return

        df.to_sql(
            table_name,
            self.engine,
            schema="curated",
            if_exists="replace",
            index=False,
            method="multi"
        )
        print(f"[INFO] Tabela {table_name} carregada em curated")

# Executar
if __name__ == "__main__":
    transform = Transform()
    transform.run()
