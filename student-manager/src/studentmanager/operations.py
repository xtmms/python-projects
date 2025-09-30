from .data import get_data, save_data, load_data, FILENAME

def show_students():
    """Display all students in the data."""
    data = get_data()
    for student in data:
        if student:  # Skip empty dictionaries
            print(f"ID: {student.get('id')}, Name: {student.get('name')}, Age: {student.get('age')}")
        else:
            print("No students found.")
        
def add_student():
    """Add a new student to the data."""
    data = get_data()
    id = input("Enter student ID: ")
    name = input("Enter student Name: ")
    age = input("Enter student Age: ")
    data.append({"id": id, "name": name, "age": age})
    save_data(data)
    
def delete_student():
    """Delete a student from the data by ID."""
    data = get_data()
    id = input("Enter student ID to delete: ")
    data = [student for student in data if student.get('id') != id]
    save_data(data)
    
def update_student():
    """Update a student's information by ID."""
    data = get_data()
    field = input("Enter field to update (id, name, age): ")
    value = input(f"Enter new value for {field}: ")
    id = input("Enter student ID to update: ")
    for student in data:
        if student.get('id') == id:
            student[field] = value
            break
    save_data(data)
    
def find_student():
    """Find and display a student by a specific field."""
    data = get_data()
    field = input("Enter field to search by (id, name, age): ")
    value = input(f"Enter value for {field}: ")
    try:
        for student in data:
                if student.get(field) == value:
                    print(f"ID: {student.get('id')}, Name: {student.get('name')}, Age: {student.get('age')}")
    except Exception as e:
        print(f"Error occurred while finding student: {e}")
        
def delete_all_students():
    """Delete all students from the data."""
    save_data([{}])