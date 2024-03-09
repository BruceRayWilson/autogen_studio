# filename: init_repo_direct.py
import os
import subprocess

def init_repo(directory: str):
    """
    Initializes a Git repository in the specified directory.
    If the directory does not exist, it is created.
    """
    # Expand the user's home directory symbol '~' to the full path
    directory = os.path.expanduser(directory)
    
    # Check if the directory exists
    if not os.path.exists(directory):
        # Create the directory if it does not exist
        os.makedirs(directory)
        print(f"Directory '{directory}' was created.")
    else:
        print(f"Directory '{directory}' already exists.")
    
    # Change the current working directory to the specified directory
    os.chdir(directory)
    
    # Initialize the Git repository
    result = subprocess.run(["git", "init"], capture_output=True, text=True)
    if result.returncode == 0:
        print("Git repository initialized successfully.")
    else:
        print("Failed to initialize Git repository:", result.stderr)

# Initialize a Git repository in the specified directory
init_repo("~/dl/github.com/BruceRayWilson/junk")