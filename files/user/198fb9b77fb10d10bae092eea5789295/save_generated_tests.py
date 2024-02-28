# filename: save_generated_tests.py
import os

def save_text_to_file(file_path: str, text: str):
    """
    Saves a given text string to a specified file path. If the directory
    for the file does not exist, it is created. If the file already exists,
    it will be overwritten.
    
    Args:
    file_path (str): The path to the file where the text will be saved.
    text (str): The text string to save to the file.
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

# The directory where the files should be saved
directory = '/home/wilsonb/dl/github.com/BruceRayWilson/Accounting'

# The generated header content from the task output
h_content = """// Struct from the first provided section.
... (rest of the header content) ...
};"""

# The generated C++ content from the task output
cpp_content = """#include "gmock/gmock.h"
... (rest of the C++ content) ...
}"""

# Save the header content to Accounting_test.h
save_text_to_file(os.path.join(directory, 'Accounting_test.h'), h_content)

# Save the C++ content to Accounting_test.cpp
save_text_to_file(os.path.join(directory, 'Accounting_test.cpp'), cpp_content)