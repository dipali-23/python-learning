# import psycopg2

# def connect_to_db():
#     """Connect to the PostgreSQL database and return the connection and cursor."""
#     conn = psycopg2.connect(
#         host="localhost",
#         database="learning",
#         user="postgres",
#         password="postgres"
#     )
#     c = conn.cursor()
#     return conn, c

# def create_table(c, conn):
#     """Create the products table if it doesn't exist."""
#     create_table_query = """
#     CREATE TABLE IF NOT EXISTS products (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(255) NOT NULL,
#         price NUMERIC(10, 2) NOT NULL,
#         quantity INTEGER NOT NULL
#     );
#     """
#     c.execute(create_table_query)
#     conn.commit()
#     print("Table created successfully.")

# db.py
import psycopg2

def connect_to_db():
    conn = psycopg2.connect(
        host="localhost",
        database="learning",
        user="postgres",
        password="postgres"
    )
    c = conn.cursor()
    return conn, c

def create_table(c, conn):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        price NUMERIC(10, 2) NOT NULL,
        quantity INTEGER NOT NULL
    );
    """
    c.execute(create_table_query)
    conn.commit()
