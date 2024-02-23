# filename: git_commit.py
import subprocess
import os

def git_commit(directory: str, commit_message: str):
    """
    Performs a Git commit in the specified directory with the given commit message.
    The function checks if the directory is a valid Git repository and if there are changes to commit.
    
    Args:
    directory (str): The path to the directory where the Git repository is located.
    commit_message (str): The commit message for the Git commit.
    """
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    # Check if the directory is a Git repository
    if not os.path.isdir(os.path.join(directory, ".git")):
        print(f"Error: The directory '{directory}' is not a Git repository.")
        return
    
    # Change the current working directory to the specified directory
    os.chdir(directory)
    
    # Add all changes to staging
    subprocess.run(["git", "add", "."])
    
    # Perform the Git commit
    result = subprocess.run(["git", "commit", "-m", commit_message], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Git commit was successful.")
    else:
        print(f"Failed to commit changes: {result.stderr}")

# Set the directory where your git repository is located
repo_directory = "/home/wilsonb/dl/github.com/BruceRayWilson/pytest-test001"
# Set your commit message
commit_message = "My latest updates."

# Perform the git commit
git_commit(repo_directory, commit_message)