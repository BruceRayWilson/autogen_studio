# filename: init_repo_script.py
import os
import subprocess

def init_repo(directory: str):
    """
    Initializes a Git repository in the specified directory.
    If the directory does not exist, it is created.
    
    Args:
    directory (str): The path to the directory where the Git repository will be initialized.
    """
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

# Initialize the directory as a Git repository
init_repo("/home/wilsonb/dl/github.com/BruceRayWilson/pytest-test001")