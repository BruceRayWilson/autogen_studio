# filename: git_commit.py
import subprocess
import os

def git_commit(directory: str, commit_message: str):
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    if not os.path.isdir(os.path.join(directory, ".git")):
        print(f"Error: The directory '{directory}' is not a Git repository.")
        return

    os.chdir(directory)
    subprocess.run(["git", "add", "."])

    result = subprocess.run(["git", "commit", "-m", commit_message], capture_output=True, text=True)

    if result.returncode == 0:
        print("Git commit was successful.")
    else:
        print(f"Failed to commit changes: {result.stderr}")

git_commit("/home/wilsonb/dl/github.com/BruceRayWilson/Accounting", "404 Error")