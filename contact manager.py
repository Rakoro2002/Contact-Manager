# 📇 Contact Manager with Names and Phone Numbers

# List of contacts, each as a dictionary
contacts = [
    {"name": "Alice", "phone": "0712345678"},
    {"name": "Bob", "phone": "0723456789"},
    {"name": "Charlie", "phone": "0734567890"}
]

# Set to track unique names
unique_names = set(contact["name"] for contact in contacts)


# Function to add a new contact
def add_contact(name, phone):
    if name in unique_names:
        print(f"{name} is already in your contacts.")
    else:
        contacts.append({"name": name, "phone": phone})
        unique_names.add(name)
        print(f"{name} has been added with phone number {phone}.")


# Function to display contacts in a table
def show_contacts():
    print("\n📋 Your Contacts:")
    print(f"{'Name':<15} {'Phone Number':<15}")
    print("-" * 30)
    for contact in sorted(contacts, key=lambda x: x["name"]):
        print(f"{contact['name']:<15} {contact['phone']:<15}")


# Main program loop
print("Welcome to Contact Manager!")
while True:
    action = input("\nChoose an action: [add/show/exit]: ").strip().lower()

    if action == "add":
        new_name = input("Enter the name to add: ").strip().title()
        new_phone = input("Enter the phone number: ").strip()
        add_contact(new_name, new_phone)
    elif action == "show":
        show_contacts()
    elif action == "exit":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid option. Please choose add, show, or exit.")
