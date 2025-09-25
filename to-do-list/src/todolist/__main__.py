from todolist import show_menu, get_user_choice, add_task, remove_task, view_tasks, load_tasks, save_tasks

def main():
    """Main function to run the To-Do List application."""
    tasks = load_tasks()
    while True:
        show_menu()
        choice = get_user_choice()
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == 'q':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
