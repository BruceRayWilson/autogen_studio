

##### Begin of git_commit #####

import subprocess
import os
from autogen.core import skill

@skill("git_commit")
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

# Example usage:
# git_commit("/path/to/repository", "Initial commit")


#### End of git_commit ####

        

##### Begin of read_file_contents #####

import os
from autogen.core import skill

@skill("read_file_contents")
def read_file_contents(file_path: str) -> str:
    """
    Reads and returns the contents of a file specified by the file path.
    If the file does not exist, an error message is returned.
    
    Args:
    file_path (str): The path to the file whose contents need to be read.
    
    Returns:
    str: The contents of the file or an error message if the file does not exist.
    """
    # Check if the file exists
    if not os.path.isfile(file_path):
        return f"Error: The file '{file_path}' does not exist."
    
    # Read the contents of the file
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
        return contents
    except Exception as e:
        return f"Error reading file '{file_path}': {e}"

# Example usage:
# contents = read_file_contents("/path/to/file.txt")
# print(contents)


#### End of read_file_contents ####

        

##### Begin of save_text_to_file #####

import os
from autogen.core import skill

@skill("save_text_to_file")
def save_text_to_file(file_path: str, text: str):
    """
    Saves a given text string to a specified file path. If the directory
    for the file does not exist, it is created. If the file already exists,
    it will be overwritten.
    
    Args:
    file_path (str): The path to the file where the text will be saved.
    text (str): The text string to save to the file.
    """
    # Extract the directory from the file_path
    directory = os.path.dirname(file_path)
    
    # Check if the directory exists
    if not os.path.exists(directory):
        # Create the directory if it does not exist
        os.makedirs(directory)
        print(f"Directory '{directory}' was created.")
    
    # Save the text to the specified file
    with open(file_path, 'w') as file:
        file.write(text)
    print(f"Text was saved to '{file_path}' successfully.")

# Example usage:
# save_text_to_file("/path/to/file.txt", "Hello, world!")


#### End of save_text_to_file ####

        

##### Begin of publish_github_repo #####

import os
import subprocess
from autogen.core import skill

@skill("publish_github_repo")
def publish_github_repo(directory: str, github_repo_url: str, git_config_done: bool = False, user_name: str = None, user_email: str = None):
    """
    Publishes the specified directory as a GitHub repository. Initializes the directory with `git init` if necessary.
    Optionally configures git user name and email.
    
    Args:
    directory (str): The path to the directory to be published.
    github_repo_url (str): The URL of the GitHub repository to push to.
    git_config_done (bool): Indicates if git config for user name and email has already been done.
    user_name (str): The user name for git config. Required if git_config_done is False.
    user_email (str): The user email for git config. Required if git_config_done is False.
    """
    # Ensure the directory exists and initialize it with git if needed
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' was created.")
    os.chdir(directory)
    if not os.path.exists(".git"):
        subprocess.run(["git", "init"], check=True)
        print("Git repository initialized successfully.")
    
    # Check if git config is needed
    if not git_config_done:
        # If user name or email is not provided, prompt the user (conceptual; replace with your input method)
        if not user_name:
            user_name = input("Please enter your Git user name: ")
        if not user_email:
            user_email = input("Please enter your Git user email: ")
        
        # Set up git configuration
        subprocess.run(["git", "config", "user.name", user_name], check=True)
        subprocess.run(["git", "config", "user.email", user_email], check=True)
    
    # Add all files to the repo and commit them
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)
    
    # Add the remote GitHub repo and push
    subprocess.run(["git", "remote", "add", "origin", github_repo_url], check=True)
    subprocess.run(["git", "push", "-u", "origin", "master"], check=True)
    print("Repository has been successfully published to GitHub.")

# Example usage:
# publish_github_repo("/path/to/directory", "https://github.com/username/repo.git", False)


#### End of publish_github_repo ####

        

##### Begin of init_repo #####

import os
import subprocess
from autogen.core import skill

@skill("init_repo")
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

# Example usage:
# init_repo("/path/to/directory")


#### End of init_repo ####

        