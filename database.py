# import sqlite3

# conn=sqlite3.connect('database.db')
# c=conn.cursor()

# create_table = """
# CREATE TABLE IF NOT EXISTS items (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     description TEXT NOT NULL,
#     price REAL NOT NULL,
#     quantity INTEGER NOT NULL
# );
# """
# c.execute(create_table)
# conn.commit()

# def add_item(name, description, price, quantity):
#     c.execute("INSERT INTO items (name, description, price, quantity) VALUES (?, ?, ?, ?)", (name, description, price, quantity))
#     conn.commit()
#     print(f"Item '{name}' added to the database.")

# def view_items():
#     c.execute("SELECT * FROM items")
#     items = c.fetchall()
#     for item in items:
#         print(f"ID: {item[0]}, Name: {item[1]}, Description: {item[2]}, Price: {item[3]}, Quantity: {item[4]}")

# def update_item(item_id, name=None, description=None, price=None, quantity=None):
#     if name:
#         c.execute("UPDATE items SET name = ? WHERE id = ?", (name, item_id))
#     if description:
#         c.execute("UPDATE items SET description = ? WHERE id = ?", (description, item_id))
#     if price:
#         c.execute("UPDATE items SET price = ? WHERE id = ?", (price, item_id))
#     if quantity:
#         c.execute("UPDATE items SET quantity = ? WHERE id = ?", (quantity, item_id))
#     conn.commit()
#     print(f"Item with ID {item_id} updated.")

# def delete_item(item_id):
#     c.execute("DELETE FROM items WHERE id = ?", (item_id,))
#     conn.commit()
#     print(f"Item with ID {item_id} deleted.")

# def close_connection():
#     conn.close()
#     print("Database connection closed.")

# # Example usage
# add_item("Laptop", "A high-performance laptop", 1200.99, 10)
# add_item("Smartphone", "A latest model smartphone", 799.99, 20)
# view_items()
# update_item(1, price=1150.00)
# delete_item(2)
# view_items()
# close_connection()




# postgresql

import psycopg2

conn=psycopg2.connect(
    host="localhost",
    database="learning",
    user="postgres",
    password="postgres",
    
)

c=conn.cursor()

create_table = """
CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    quantity INTEGER NOT NULL
);
"""
c.execute(create_table)
conn.commit()
def add_item(name, description, price, quantity):
    c.execute("INSERT INTO items (name, description, price, quantity) VALUES (%s, %s, %s, %s)", (name, description, price, quantity))
    conn.commit()
    print(f"Item '{name}' added to the database.")
def view_items():
    c.execute("SELECT * FROM items")
    items = c.fetchall()
    for item in items:
        print(f"ID: {item[0]}, Name: {item[1]}, Description: {item[2]}, Price: {item[3]}, Quantity: {item[4]}")
def update_item(item_id, name=None, description=None, price=None, quantity=None):   
    if name:
        c.execute("UPDATE items SET name = %s WHERE id = %s", (name, item_id))
    if description:
        c.execute("UPDATE items SET description = %s WHERE id = %s", (description, item_id))
    if price:
        c.execute("UPDATE items SET price = %s WHERE id = %s", (price, item_id))
    if quantity:
        c.execute("UPDATE items SET quantity = %s WHERE id = %s", (quantity, item_id))
    conn.commit()
    print(f"Item with ID {item_id} updated.")
def delete_item(item_id):
    c.execute("DELETE FROM items WHERE id = %s", (item_id,))
    conn.commit()
    print(f"Item with ID {item_id} deleted.")
def close_connection():
    conn.close()
    print("Database connection closed.")
# Example usage
add_item("Laptop", "A high-performance laptop", 1200.99, 10)
add_item("Smartphone", "A latest model smartphone", 799.99, 20)
view_items()
update_item(1, price=1150.00)
delete_item(2)
view_items()
close_connection()
