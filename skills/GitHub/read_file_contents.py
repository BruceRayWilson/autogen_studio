import os
from autogen.core import skill

@skill("read_file_contents")
def read_file_contents(file_path: str) -> str:
    """
    Reads and returns the contents of a file specified by the file path.
    If the file does not exist, an error message is returned.
    
    Args:
    file_path (str): The path to the file whose contents need to be read.
    
    Returns:
    str: The contents of the file or an error message if the file does not exist.
    """
    # Check if the file exists
    if not os.path.isfile(file_path):
        return f"Error: The file '{file_path}' does not exist."
    
    # Read the contents of the file
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
        return contents
    except Exception as e:
        return f"Error reading file '{file_path}': {e}"

# Example usage:
# contents = read_file_contents("/path/to/file.txt")
# print(contents)
