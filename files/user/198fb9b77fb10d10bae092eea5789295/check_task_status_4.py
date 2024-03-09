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
    command = f"curl http://127.0.0.1:5000/check-status/{task_id}"
    
    # Use shlex.split to ensure the command is properly split for subprocess
    args = shlex.split(command)
    
    try:
        # Execute the curl command
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check if the output is empty and return a message if so
        if result.stdout.strip() == "":
            return "The server returned an empty response."
        else:
            # Return the standard output from curl command
            return result.stdout
    except subprocess.CalledProcessError as e:
        # Return the standard error if the command failed
        return f"Command failed with error: {e.stderr}"

# The task ID to check
task_id = "58deef94-8a28-4a4e-a9c3-e3dd7d4cab7f"

# Call the function to check the status of the task
status_output = check_task_id_status(task_id)
print(status_output)