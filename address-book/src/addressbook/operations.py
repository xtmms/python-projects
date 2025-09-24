import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

def show_menu():
    logging.info("Address Book Menu:")
    logging.info("1. View Contacts")
    logging.info("2. Add Contact")
    logging.info("3. Delete Contact")
    logging.info("q. Exit")

def get_user_choice():
    choice = input("Enter your choice (1-4): ")
    return choice

def display_contacts(contacts):
    if not contacts:
        logging.info("No contacts found.")
        return
    for name, info in contacts.items():
        logging.info(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")


def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone: ")
    email = input("Enter contact email: ")
    contacts[name] = {"phone": phone, "email": email}
    logging.info(f"Contact {name} added.")

def delete_contact(contacts):
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        logging.info(f"Contact {name} deleted.")
    else:
        logging.info(f"Contact {name} not found.")