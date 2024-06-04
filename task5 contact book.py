import json

def load_contacts(filename='contacts.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(contacts, filename='contacts.json'):
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ").strip().lower()
    results = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]
    
    if results:
        for contact in results:
            print(f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n")
    else:
        print("No contacts found.")

def update_contact(contacts):
    search_term = input("Enter the name of the contact to update: ").strip().lower()
    for contact in contacts:
        if search_term == contact['name'].lower():
            print("Contact found. Enter new details (leave blank to keep current value).")
            contact['name'] = input(f"Name ({contact['name']}): ") or contact['name']
            contact['phone'] = input(f"Phone ({contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"Email ({contact['email']}): ") or contact['email']
            contact['address'] = input(f"Address ({contact['address']}): ") or contact['address']
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact(contacts):
    search_term = input("Enter the name of the contact to delete: ").strip().lower()
    for contact in contacts:
        if search_term == contact['name'].lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
