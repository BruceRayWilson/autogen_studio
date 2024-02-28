# filename: create_unit_tests_direct.py
import os
import json
import subprocess

def create_unit_tests(parent_dir: str, uut_dir: str = 'UUT', src_dir: str = 'src'):
    base_url = 'http://127.0.0.1:5000/'
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
                        try:
                            data = json.loads(result.stdout)
                            if 'status' in data and data['status'] == 200:
                                if 'id' in data:
                                    print(f"Processing started for {file_name}. Task ID: {data['id']}")
                                    return data['id']
                                else:
                                    print(f"Error: {data.get('message')}")
                        except json.JSONDecodeError:
                            print(f"Non-JSON response received: {result.stdout}")
                    else:
                        print(f"Failed to submit files. Command exited with return code: {result.returncode}")
                        print(f"Error: {result.stderr}")

            else:
                print(f"Matching .h file not found for {file_name}")

# Set the parent directory where the UUT and src directories are located
parent_dir = '/home/wilsonb/dl/github.com/BruceRayWilson/Accounting'

# Call the function to create unit tests
task_id = create_unit_tests(parent_dir)

# If a task ID was received, print it
if task_id:
    print(f"Use the following command to check the status of the task:")
    print(f"curl http://127.0.0.1:5000/check-status/{task_id}")