# filename: commit_all_files.py
import subprocess
import os

# Function to perform a Git commit in the specified directory with a given commit message
def git_commit(directory: str, commit_message: str):
    # Check if the directory is a valid Git repository
    if not os.path.isdir(os.path.join(directory, ".git")):
        print(f"Error: The directory '{directory}' is not a Git repository.")
        return
    
    # Change the current working directory to the specified directory
    os.chdir(directory)
    
    # Add all changes to staging
    subprocess.run(["git", "add", "."], check=True)
    
    # Perform the Git commit
    result = subprocess.run(["git", "commit", "-m", commit_message], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Git commit was successful.")
    else:
        print(f"Failed to commit changes: {result.stderr}")

# Specify the correct directory
correct_directory = "/home/wilsonb/dl/github.com/BruceRayWilson/pytest-test001"

# Commit all the files in the correct directory with a commit message
git_commit(correct_directory, "Commit all files in the directory")