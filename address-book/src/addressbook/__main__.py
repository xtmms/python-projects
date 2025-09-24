from .operations import show_menu, get_user_choice, display_contacts, add_contact, delete_contact
from .data import load_contacts, save_contacts

def main():
    """Main function to run the address book application."""
    contacts = load_contacts()
    while True:
        show_menu()
        choice = get_user_choice()
        try:

            if choice == "1":
                display_contacts(contacts)
            elif choice == "2":
                add_contact(contacts)
            elif choice == "3":
                delete_contact(contacts)
            elif choice == "q":
                save_contacts(contacts)
                print("Exiting...")
                break

        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")

if __name__ == "__main__":
    main()

