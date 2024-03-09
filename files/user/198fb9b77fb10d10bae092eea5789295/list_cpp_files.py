# filename: list_cpp_files.py
import os

# Define the parent directory where the C++ files are located
parent_dir = os.path.expanduser('~/dl/github.com/BruceRayWilson/Accounting')

# List all .cpp files in the directory
cpp_files = [f for f in os.listdir(parent_dir) if f.endswith('.cpp')]

# Print the list of .cpp files
print("List of .cpp files in the directory:")
for cpp_file in cpp_files:
    print(cpp_file)

# Check if there are any .cpp files
if not cpp_files:
    print("No .cpp files found in the directory.")