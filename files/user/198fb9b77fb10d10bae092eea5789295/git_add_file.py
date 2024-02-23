# filename: git_add_file.py
import subprocess
import os

# Set the path to your repository
repo_path = '/home/wilsonb/dl/github.com/BruceRayWilson/pytest-test001'
file_name = 'database.sqlite'

# Check if the repository path exists
if not os.path.exists(repo_path):
    print(f"Error: The directory '{repo_path}' does not exist.")
else:
    # Check if the repository path is a Git repository
    if not os.path.isdir(os.path.join(repo_path, ".git")):
        print(f"Error: The directory '{repo_path}' is not a Git repository.")
    else:
        # Change the current working directory to the repository path
        os.chdir(repo_path)
        
        # Add the file to the staging area
        result = subprocess.run(["git", "add", file_name], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"The file '{file_name}' has been successfully staged for commit.")
        else:
            print(f"Failed to add the file '{file_name}' to staging: {result.stderr}")