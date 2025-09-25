import json

FILENAME = "tasks.json"

def load_tasks(file_path=FILENAME):
    """Load tasks from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        tasks = []
        return tasks
    except json.JSONDecodeError:
        tasks = []
        return tasks

def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open(FILENAME, 'w') as file:
        json.dump(tasks, file, indent=4)