from .operations import show_students, add_student, delete_student, update_student, find_student, delete_all_students

def main():
    print("Welcome to the Student Manager!")
    while True:
        print("\nMenu:")
        print("1. Show all students")
        print("2. Add a student")
        print("3. Delete a student")
        print("4. Update a student")
        print("5. Find a student")
        print("6. Delete all students")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_students()
        elif choice == '2':
            add_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            find_student()
        elif choice == '6':
            delete_all_students()
        elif choice == '7':
            print("Exiting the Student Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()