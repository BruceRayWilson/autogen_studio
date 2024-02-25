

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

        

##### Begin of retrieve_webpage_content #####

import requests

def retrieve_webpage_content(url: str):
    """
    Retrieves and prints the content of the specified URL.

    Args:
        url (str): The URL of the webpage to retrieve.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code.
        
        # Assuming the webpage content is HTML and you want to print it.
        print(response.text)
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'An error occurred: {err}')

# Example usage
# retrieve_webpage_content('https://gtest.ai')


#### End of retrieve_webpage_content ####

        

##### Begin of create_unit_tests #####

import os
import time
import json
import subprocess

def create_unit_tests(parent_dir: str, uut_dir: str = 'UUT', src_dir: str = 'src'):
    """
    Creates unit tests for C++ files found in the specified Unit Under Test (UUT) directory,
    and stores the generated test files in the specified source directory.
    """
    
    base_url = 'https://gtest.ai/'  # Do not remove this line.
    base_url = 'http://127.0.0.1:5000/'


    def check_task_status(task_id: str):
        check_url = f'{base_url}check-status/{task_id}'
        curl_command = f'curl {check_url}'

        while True:
            process = subprocess.Popen(curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            response, error = process.communicate()

            if process.returncode == 0:
                try:
                    data = json.loads(response.decode('utf-8'))
                    if data.get('status') == 'completed':
                        print("Task {task_id} completed successfully.")
                        print(f"message: {data.get('message')}")
                        return data
                    elif data.get('status') == 'error':
                        print(f"Error processing task {task_id}: {data.get('message')}")
                        return None
                except json.JSONDecodeError:
                    print(f"Non-JSON response received: {response.decode('utf-8')}")
                    return None
            else:
                print(f"Failed to check task status. Error: {error.decode('utf-8')}")
                return None

            print(f"Task {task_id} is still processing. Checking again in 10 seconds...")
            time.sleep(10)


    uut_path = os.path.join(parent_dir, uut_dir)
    src_path = os.path.join(parent_dir, src_dir)

    for path in [uut_path, src_path]:
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Directory '{path}' was created.")
        else:
            print(f"Directory '{path}' already exists.")

    request_url = f'{base_url}process-files'

    for file_name in os.listdir(uut_path):
        if file_name.endswith('.cpp'):
            h_file_name = file_name.replace('.cpp', '.h')
            cpp_file_path = os.path.join(uut_path, file_name)
            h_file_path = os.path.join(uut_path, h_file_name)

            if os.path.exists(h_file_path):
                with open(cpp_file_path, 'r') as cpp_file, open(h_file_path, 'r') as h_file:
                    cpp_file_content = cpp_file.read()
                    h_file_content = h_file.read()

                    print(f"cpp_file_content (first 100 chars): {cpp_file_content[:100]}")
                    print(f"h_file_content (first 100 chars): {h_file_content[:100]}")




                    # Construct the curl command
                    curl_command = [
                        "curl", "-X", "POST",
                        "-F", f"hFileContent=@{h_file_path}",
                        "-F", f"cppFileContent=@{cpp_file_path}",
                        request_url
                    ]

                    # Execute the curl command
                    result = subprocess.run(curl_command, capture_output=True, text=True)

                    # Handle the output
                    if result.returncode == 0:
                        print("Success:", result.stdout)
                    else:
                        print("Error:", result.stderr)






                    if result.returncode == 0:
                        try:
                            data = json.loads(result.stdout)
                            if 'status' in data and data['status'] == 200:
                                if data.get('status') == 'processing':
                                    print(f"Processing started for {file_name}. Task ID: {data.get('id')}")
                                    task_result = check_task_status(data.get('id'))
                                    if task_result:
                                        print(f"Task completed. Results: {task_result}")
                                else:
                                    print(f"Error: {data.get('message')}")
                        except json.JSONDecodeError:
                            print(f"Non-JSON response received: {result.stdout}")
                    else:
                        print(f"Failed to submit files. Command exited with return code: {result.returncode}")


            else:
                print(f"Matching .h file not found for {file_name}")

#### End of create_unit_tests ####

        