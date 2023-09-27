import json
import os

def save_data(data, filename):
    serialized_data = [item.__dict__ for item in data]
    with open(filename, 'w') as file:
        json.dump(serialized_data, file)

def ensure_files_exist():
    filenames = ['books.json', 'people.json', 'rentals.json']
    for filename in filenames:
        if not os.path.exists(filename):
            print(f"{filename} file not found. Creating a new one")
            with open(filename, 'w') as file:
                json.dump([], file)

def load_data_from_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            json_data = file.read()
            return json.loads(json_data)
    else:
        print(f"{filename} file not found. Creating a new one")
        return []

# Example usage:
# ensure_files_exist()
# data = load_data_from_file('books.json')
# save_data(data, 'books.json')
