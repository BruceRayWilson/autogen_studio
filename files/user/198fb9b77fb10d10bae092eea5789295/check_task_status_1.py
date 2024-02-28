# filename: check_task_status.py
import subprocess
import shlex
import json

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
        
        # Print the raw output from the server
        print("Raw server response:")
        print(result.stdout)
        
        # Return the standard output from curl command
        return result.stdout
    except subprocess.CalledProcessError as e:
        # Print the raw error output from the server
        print("Raw server error response:")
        print(e.stderr)
        # Return the standard error if the command failed
        return f"Command failed with error: {e.stderr}"

# The task ID from the previous operation
task_id = "d4579a89-0a5f-4c9f-8a0e-5ada82de397f"

# Check the status of the task
status_output = check_task_id_status(task_id)

# Attempt to parse the JSON output and take action based on the status
try:
    status_data = json.loads(status_output)
    if status_data['status'] == 'completed':
        print("Task completed successfully.")
        # Here you can handle the completed status, e.g., download test files if provided by the service
    elif status_data['status'] == 'processing':
        print("Task is still processing. Please check again later.")
    else:
        print(f"Task status unknown: {status_data}")
except json.JSONDecodeError:
    print("Failed to parse JSON response. The raw response is printed above.")