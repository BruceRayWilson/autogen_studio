# filename: update_create_unit_tests.py

import os

# Path to the create_unit_tests.py file
file_path = '/home/wilsonb/dl/github.com/BruceRayWilson/Accounting/create_unit_tests.py'

# Check if the file exists
if not os.path.isfile(file_path):
    print(f"Error: The file '{file_path}' does not exist.")
else:
    # Read the contents of the file
    with open(file_path, 'r') as file:
        contents = file.readlines()

    # Update the contents
    updated_contents = []
    for line in contents:
        if "print(f\"JSON payload: {json.dumps(json_payload)[:100]}\")" in line:
            updated_contents.append("print(f\"JSON payload: {json.dumps(json_payload)}\")\n")
        else:
            updated_contents.append(line)

    # Write the updated contents back to the file
    with open(file_path, 'w') as file:
        file.writelines(updated_contents)
    print(f"File '{file_path}' has been updated successfully.")