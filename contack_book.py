contacts ={}

while True:
    action = input("Do you want to add, view,update, search,count, or exit? (add/view/update/search/count/exit): ").strip().lower()
    
    if action == 'add':
        name = input("Enter contact name: ").strip()
        phone = input("Enter contact phone number: ").strip()
        contacts[name] = phone
        print(f"Contact '{name}' added successfully.")

    elif action == 'view':
        if contacts:
            print("Contact List:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found.")

    elif action == 'search':
        name = input("Enter contact name to search: ").strip()
        if name in contacts:
            print(f"Contact found - {name}: {contacts[name]}")
        else:
            print(f"Contact '{name}' not found.")
    elif action == 'update':
        name = input("Enter contact name to update: ").strip()
        if name in contacts:
            new_phone = input(f"Enter new phone number for '{name}': ").strip()
            contacts[name] = new_phone
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")
        count = len(contacts)
        print(f"Total number of contacts: {count}")
    
    elif action == 'count':
        count = len(contacts)
        print(f"Total number of contacts: {count}")

    elif action == 'exit':
        print("Exiting the contact book.")
        break

    else:
        print("Invalid action. Please choose add, view, search, or exit.")

