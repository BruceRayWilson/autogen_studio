# filename: check_task_status.py
import subprocess
import json

# The task ID you want to check
task_id = "0cd490c2-1a66-4126-90a6-7dff94672843"

# The URL to check the task status
check_url = f"http://127.0.0.1:5000/check-status/{task_id}"

# The curl command
curl_command = f"curl {check_url}"

# Execute the curl command
process = subprocess.Popen(curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
response, error = process.communicate()

if process.returncode == 0:
    try:
        # Attempt to parse the JSON response
        data = json.loads(response.decode('utf-8'))
        print(f"Response: {data}")
    except json.JSONDecodeError:
        # If response is not JSON, print the raw response
        print(f"Non-JSON response received: {response.decode('utf-8')}")
else:
    print(f"Error: {error.decode('utf-8')}")