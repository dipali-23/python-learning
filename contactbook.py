import json

def load_contacts(file='contactbook.json'):
    try:
        with open(file, 'r') as f:
            content = f.read()
            if not content.strip():
                return []
            return json.loads(content)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_contacts(contacts, file='contactbook.json'):
    with open(file, 'w') as f:
        json.dump(contacts, f, indent=4)

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contact = {'name': name, 'phone': phone}
    contacts = load_contacts()
    contacts.append(contact)
    save_contacts(contacts)
    print(f"Contact {name} added.")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}")

def delete_contact():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    view_contacts()
    try:
        index = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            save_contacts(contacts)
            print(f"Deleted contact: {deleted_contact['name']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def search_contact():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    name = input("Enter the name to search: ")
    found_contacts = [contact for contact in contacts if name.lower() in contact['name'].lower()]
    if found_contacts:
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    else:
        print("No contacts found with that name.")

def main():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            print("Exiting the contact book.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
