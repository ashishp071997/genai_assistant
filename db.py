# db.py
import duckdb
import os
#genai_assistant/
db_path = "genai_assistant/db/analytics.db"

# Ensure directory exists
os.makedirs("db", exist_ok=True)

# DuckDB will CREATE the DB if it does not exist
#con = duckdb.connect(db_path)

def init_db():
   
    con = duckdb.connect(db_path)

    con.execute("""
    DROP TABLE IF EXISTS customers;
    DROP TABLE IF EXISTS orders;
    DROP TABLE IF EXISTS order_items;
    DROP TABLE IF EXISTS products;
                
    CREATE TABLE customers AS SELECT * FROM read_csv_auto('genai_assistant/data/customers.csv');
    CREATE TABLE orders AS SELECT * FROM read_csv_auto('genai_assistant/data/orders.csv');
    CREATE TABLE order_items AS SELECT * FROM read_csv_auto('genai_assistant/data/order_items.csv');
    CREATE TABLE products AS SELECT * FROM read_csv_auto('genai_assistant/data/products.csv');
    """)
    return con


def get_customer_spend(con, customer_name):
    query = f"""
    SELECT
        c.name,
        SUM(oi.quantity * p.price) AS total_spend
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.product_id
    WHERE c.name = '{customer_name}'
    GROUP BY c.name
    """
    return con.execute(query).fetchone()
