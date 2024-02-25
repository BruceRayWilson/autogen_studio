# filename: find_create_unit_tests.py

import os

def find_file(root_folder, file_name):
    for root, dirs, files in os.walk(root_folder):
        if file_name in files:
            return os.path.join(root, file_name)
    return None

# Define the root folder and the file name to search for
root_folder = '/home/wilsonb/dl/github.com/BruceRayWilson/Accounting'
file_name = 'create_unit_tests.py'

# Search for the file
file_path = find_file(root_folder, file_name)

# Print the result
if file_path:
    print(f"File found: {file_path}")
else:
    print(f"File '{file_name}' not found in '{root_folder}' or its subdirectories.")