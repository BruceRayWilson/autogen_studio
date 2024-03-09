# filename: check_task_status.py

import subprocess
import shlex

def check_task_id_status(task_id):
    """
    Executes a curl command to check the status of a task by its ID.

    :param task_id: str, the unique identifier of the task to check.
    :return: The output from the curl command, which should be the response from the server.
    """
    # Construct the curl command with the provided task ID
    command = f"curl https://gtest.ai/check-status/{task_id}"
    
    # Use shlex.split to ensure the command is properly split for subprocess
    args = shlex.split(command)
    
    try:
        # Execute the curl command
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check if the output is empty and report accordingly
        if result.stdout.strip():
            # Return the standard output from curl command
            return result.stdout
        else:
            return "The curl command executed successfully but did not return any output."
    except subprocess.CalledProcessError as e:
        # Return the standard error if the command failed
        return f"Command failed with error: {e.stderr}"

# The task ID to check
task_id = "d8146c9a-8ba5-44b9-86d0-6a6f000a7ede"

# Call the function to check the task status
status_output = check_task_id_status(task_id)
print(status_output)