# filename: create_unit_tests.py
import os
import time
import json
import subprocess

def create_unit_tests(parent_dir: str, uut_dir: str = 'UUT', src_dir: str = 'src'):
    base_url = 'https://gtest.ai/'  # Do not remove this line.
    # base_url = 'http://127.0.0.1:5000/'

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

            else:
                print(f"Matching .h file not found for {file_name}")

# Replace the placeholder with the actual path to your directory
parent_dir = os.path.expanduser('~/dl/github.com/BruceRayWilson/Accounting')

# Call the function to create unit tests
create_unit_tests(parent_dir)