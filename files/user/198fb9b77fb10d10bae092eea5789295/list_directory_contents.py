# filename: list_directory_contents.py
import os

# Set the directory to list
directory_to_list = '~/dl/github.com/BruceRayWilson/Accounting'

# Expand the user's home directory and list the contents
directory_to_list = os.path.expanduser(directory_to_list)
print(f"Listing contents of: {directory_to_list}")

# List the contents of the directory
try:
    for item in os.listdir(directory_to_list):
        print(item)
except FileNotFoundError:
    print(f"The directory {directory_to_list} does not exist.")
except NotADirectoryError:
    print(f"{directory_to_list} is not a directory.")
except PermissionError:
    print(f"Permission denied to list contents of {directory_to_list}.")