from logic import *
from db import connect_to_db,create_table

conn, c = connect_to_db()
create_table(c, conn)

while True:
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. View Items")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. View Low Stock Items")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        add_item(c, conn, name, price, quantity)
    elif choice == '2':
        view_items(c)
    elif choice == '3':
        item_id = int(input("Enter item ID to update: "))
        name = input("Enter new item name (leave blank to skip): ")
        price = input("Enter new item price (leave blank to skip): ")
        quantity = input("Enter new item quantity (leave blank to skip): ")
        update_item(c, conn, item_id, name if name else None, float(price) if price else None, int(quantity) if quantity else None)
    elif choice == '4':
        item_id = int(input("Enter item ID to delete: "))
        delete_item(c, conn, item_id)
    elif choice == '5':
        view_low_stock_items(c)
    elif choice == '6':
        close_connection(conn)
        break
    else:
        print("Invalid choice. Please try again.")