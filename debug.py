import duckdb
from db import init_db, get_customer_spend


init_db()  # 🔥 This creates tables in analytics.db
#genai_assistant/
con = duckdb.connect("db/analytics.db")


print(con.execute("DESCRIBE customers").fetchdf())


print(con.execute("SELECT * FROM customers LIMIT 5").fetchdf())


print(con.execute("SELECT * FROM products LIMIT 5").fetchdf())

customer_name = "John"   # <-- change based on your CSV

# 3️⃣ Get spend
result = get_customer_spend(con, customer_name)

print("\n💰 Customer Spend Result:")
if result:
    print(f"Customer: {result[0]}")
    print(f"Total Spend: {result[1]}")
else:
    print("No data found for this customer.")