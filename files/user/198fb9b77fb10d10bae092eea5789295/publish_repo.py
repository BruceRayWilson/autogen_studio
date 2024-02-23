# filename: publish_repo.py
import subprocess
import os

# Set the directory and GitHub repository URL
directory = "/home/wilsonb/dl/github.com/BruceRayWilson/pytest-test001"
github_repo_url = "https://github.com/BruceRayWilson/pytest-test001.git"

# Change to the specified directory
os.chdir(directory)

# Add the remote GitHub repo and push
try:
    subprocess.run(["git", "remote", "add", "origin", github_repo_url], check=True)
    subprocess.run(["git", "branch", "-M", "main"], check=True)
    subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
    print("Repository has been successfully published to GitHub.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")