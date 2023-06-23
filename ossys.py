import os

def file_exists(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False

# Example usage
path = 'path/to/your/file.txt'  # Replace with the actual file path

if file_exists(path):
    # File exists, proceed with opening the file
    with open(path, 'r') as file:
        # Perform your operations on the file
        # ...
        pass
else:
    print("File does not exist.")
