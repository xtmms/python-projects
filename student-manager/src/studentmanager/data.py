import json

FILENAME = "students.json"

def load_data():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [{}]

def get_data():
    return load_data()

def save_data(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)
