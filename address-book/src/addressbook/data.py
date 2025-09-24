import json

DEFAULT_FILE = "contacts.json"

def load_contacts():
    """This function loads contacts from a JSON file."""
    try:
        with open(DEFAULT_FILE, "r") as file:
            contacts = json.load(file)
    except json.JSONDecodeError:
        contacts = {}
    except FileNotFoundError:
        contacts = {}
    return contacts

def save_contacts(contacts):
    """This function saves contacts to a JSON file."""
    with open(DEFAULT_FILE, "w") as file:
        json.dump(contacts, file, indent=4)