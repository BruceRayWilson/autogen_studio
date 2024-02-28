# filename: save_h_content_to_file.py
import json

# Replace 'json_response' with the actual JSON response you have
json_response = '{"className": "Accounting", "hContent": "content of the h file"}'

# Parse the JSON response
data = json.loads(json_response)

# Extract the className and hContent
class_name = data['className']
h_content = data['hContent']

# Define the file name
file_name = f"{class_name}Fixtures.h"

# Write the hContent to the file
with open(file_name, 'w') as file:
    file.write(h_content)

print(f"Content written to {file_name}")