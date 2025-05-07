import json

def save_contacts(filename, contacts):
    try:
        with open(filename, 'w') as file:
            json.dump(contacts, file)
        print("Contacts saved successfully!")
    except Exception as e:
        print("Error saving contacts:", e)

def load_contacts(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("No contact file found. Starting with an empty contact book.")
        return {}
    except json.JSONDecodeError:
        print("Error: File is not in the correct format.")
        return {}
    except Exception as e:
        print("Error loading contacts:", e)
        return {}

def contact_book():
    filename = "contacts.json"
    contacts = load_contacts(filename)

    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            contacts[name] = phone
            save_contacts(filename, contacts)

        elif choice == '2':
            for name, phone in contacts.items():
                print(f"{name}: {phone}")

        elif choice == '3':
            print("Exiting contact book.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Run contact book
contact_book()
