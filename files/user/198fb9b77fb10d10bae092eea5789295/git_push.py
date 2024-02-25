# filename: git_push.py
import subprocess
import os

def git_push(directory: str):
    # Change the current working directory to the specified directory
    os.chdir(directory)
    
    # Perform the Git push operation
    result = subprocess.run(["git", "push"], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Git push was successful.")
    else:
        print(f"Failed to push changes: {result.stderr}")

# Replace '/path/to/your/repo' with the path to your Git repository
git_push("/home/wilsonb/dl/github.com/BruceRayWilson/pytest-test001")
