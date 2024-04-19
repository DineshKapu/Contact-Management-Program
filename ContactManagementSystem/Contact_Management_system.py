import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}
    return contacts

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def add_contact(name, phone_number, email, contacts):
    contacts[name] = {"phone": phone_number, "email": email}
    save_contacts(contacts)
    print("Contact added successfully.")

def view_contacts(contacts):
    if contacts:
        print("Contact List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("Contact list is empty.")

def edit_contact(name, phone_number, email, contacts):
    if name in contacts:
        contacts[name] = {"phone": phone_number, "email": email}
        save_contacts(contacts)
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(name, contacts):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

contacts = load_contacts()
while True:
    print("\nOptions:")
    print("1. Add new contact")
    print("2. View contacts")
    print("3. Edit contact")
    print("4. Delete contact")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(name, phone_number, email, contacts)
    elif choice == "2":
            view_contacts(contacts)
    elif choice == "3":
            name = input("Enter name of contact to edit: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            edit_contact(name, phone_number, email, contacts)
    elif choice == "4":
            name = input("Enter name of contact to delete: ")
            delete_contact(name, contacts)
    elif choice == "5":
            print("Exiting program.")
            break
    else:
            print("Invalid choice. Please try again.")

