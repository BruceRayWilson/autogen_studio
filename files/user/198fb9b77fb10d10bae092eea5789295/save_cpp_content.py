# filename: save_cpp_content.py

import os

def save_text_to_file(file_path: str, text: str):
    """
    Saves a given text string to a specified file path. If the directory
    for the file does not exist, it is created. If the file already exists,
    it will be overwritten.
    """
    # Extract the directory from the file_path
    directory = os.path.dirname(file_path)
    
    # Check if the directory exists
    if not os.path.exists(directory):
        # Create the directory if it does not exist
        os.makedirs(directory)
        print(f"Directory '{directory}' was created.")
    
    # Save the text to the specified file
    with open(file_path, 'w') as file:
        file.write(text)
    print(f"Text was saved to '{file_path}' successfully.")

# Replace the following string with the actual source content
cppContent = """
// Your source content goes here
"""

# Path to the source file
source_file_path = '/home/wilsonb/dl/github.com/BruceRayWilson/Accounting/Accounting.cpp'

# Save the source content to the file
save_text_to_file(source_file_path, cppContent)