def show_menu():
    print("To-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("q. Exit")

def get_user_choice():
    choice = input("Enter your choice (1-3 or q for Exit): ")
    return choice

def add_task(tasks):
    task = input("Enter the task description: ")
    tasks.append(task)
    print(f'Task "{task}" added.')

def remove_task(tasks):
    task = input("Enter the task description to remove: ")
    if task in tasks:
        tasks.remove(task)
        print(f'Task "{task}" removed.')
    else:
        print(f'Task "{task}" not found.')

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")