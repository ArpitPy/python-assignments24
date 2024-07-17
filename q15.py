# file_operations.py

def read_file(file_name):
    """Read and return the contents of the file."""
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{file_name}' not found."

def write_to_file(file_name, data):
    """Write data to a file (overwrite if file exists)."""
    with open(file_name, 'w') as file:
        file.write(data)

def append_to_file(file_name, data):
    """Append data to the end of a file."""
    with open(file_name, 'a') as file:
        file.write(data + "\n")
