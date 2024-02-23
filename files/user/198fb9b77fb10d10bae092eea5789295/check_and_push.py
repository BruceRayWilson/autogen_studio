# filename: check_and_push.py
import subprocess
import os

# Set the directory
directory = "/home/wilsonb/dl/github.com/BruceRayWilson/pytest-test001"

# Change to the specified directory
os.chdir(directory)

# Check for commits in the local repository
try:
    log_check = subprocess.run(["git", "log"], capture_output=True, text=True)
    if log_check.returncode == 0:
        print("Commits are present in the local repository. Attempting to push to remote...")
        # Push the changes to the remote repository
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print("Repository has been successfully pushed to GitHub.")
    else:
        print("No commits found in the local repository. Please commit changes before pushing.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")