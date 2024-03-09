# filename: list_uut_directory_contents.py
import os

# Set the parent directory where the UUT directory is located
parent_dir = '~/dl/github.com/BruceRayWilson/Accounting'
uut_dir = 'UUT'

# Expand the user's home directory and list the contents of the UUT directory
parent_dir = os.path.expanduser(parent_dir)
uut_path = os.path.join(parent_dir, uut_dir)
print(f"Listing contents of UUT directory: {uut_path}")

# List the contents of the UUT directory
try:
    for item in os.listdir(uut_path):
        print(item)
except FileNotFoundError:
    print(f"The UUT directory {uut_path} does not exist.")
except NotADirectoryError:
    print(f"{uut_path} is not a directory.")
except PermissionError:
    print(f"Permission denied to list contents of {uut_path}.")