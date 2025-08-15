import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="weather_db",  # your database name
    user="postgres",        # your PostgreSQL username
    password="160204",  # your password
    port=5432
)
print("✅ Connected to PostgreSQL successfully!")
conn.close()
