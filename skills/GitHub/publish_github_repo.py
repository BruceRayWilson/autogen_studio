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
