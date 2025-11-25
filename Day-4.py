#Build a mini contact management system using a dictionary to store contacts 
contacts = {}
def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact {name} added.")
def view_contacts():
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} not found.")
      
# Example usage
add_contact("Alice", "123-456-7890")
add_contact("Bob", "987-654-3210")
view_contacts()
delete_contact("Alice")
view_contacts()
