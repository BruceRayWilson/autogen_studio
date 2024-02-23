# filename: update_remote.py
import subprocess
import os

# Set the directory and GitHub repository URL
directory = "/home/wilsonb/dl/github.com/BruceRayWilson/pytest-test001"
github_repo_url = "https://github.com/BruceRayWilson/pytest-test001.git"

# Change to the specified directory
os.chdir(directory)

# Update the remote GitHub repo URL and push
try:
    # Check if the remote 'origin' already exists
    remote_check = subprocess.run(["git", "remote", "get-url", "origin"], capture_output=True, text=True)
    if remote_check.returncode == 0:
        # Update the existing 'origin' remote
        subprocess.run(["git", "remote", "set-url", "origin", github_repo_url], check=True)
    else:
        # Add a new 'origin' remote
        subprocess.run(["git", "remote", "add", "origin", github_repo_url], check=True)
    
    # Push the changes to the updated remote
    subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
    print("Repository has been successfully published to GitHub.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")