

def add_item(c, conn, name, price, quantity):
    """Add a new item to the inventory."""
    insert_query = """
    INSERT INTO products (name, price, quantity)
    VALUES (%s, %s, %s);
    """
    c.execute(insert_query, (name, price, quantity))
    conn.commit()
    print(f"Item '{name}' added to the inventory.")
def view_items(c):  
    """View all items in the inventory."""
    select_query = "SELECT * FROM products;"
    c.execute(select_query)
    items = c.fetchall()
    for item in items:
        print(f"ID: {item[0]}, Name: {item[1]}, Price: {item[2]}, Quantity: {item[3]}")
def update_item(c, conn, item_id, name=None, price=None, quantity=None):    
    """Update an existing item in the inventory."""
    if name:
        c.execute("UPDATE products SET name = %s WHERE id = %s", (name, item_id))
    if price:
        c.execute("UPDATE products SET price = %s WHERE id = %s", (price, item_id))
    if quantity:
        c.execute("UPDATE products SET quantity = %s WHERE id = %s", (quantity, item_id))
    conn.commit()
    print(f"Item with ID {item_id} updated.")
def delete_item(c, conn, item_id):      
    """Delete an item from the inventory."""
    c.execute("DELETE FROM products WHERE id = %s", (item_id,))
    conn.commit()
    print(f"Item with ID {item_id} deleted.")
def view_low_stock_items(c):  
    """View items with low stock (less than 5)."""
    select_query = "SELECT * FROM products WHERE quantity < 5;"
    c.execute(select_query)
    low_stock_items = c.fetchall()
    if low_stock_items:
        print("Low stock items:")
        for item in low_stock_items:
            print(f"ID: {item[0]}, Name: {item[1]}, Price: {item[2]}, Quantity: {item[3]}")
    else:
        print("No low stock items found.")
def close_connection(conn):
    """Close the database connection."""
    conn.close()
    print("Database connection closed.")

