import os
import requests
import time

def create_unit_tests(parent_dir: str, uut_dir: str = 'UUT', src_dir: str = 'src'):
    """
    Creates unit tests for C++ files found in the specified Unit Under Test (UUT) directory,
    and stores the generated test files in the specified source directory.
    """
    
    base_url = 'https://gtest.ai/'  # Do not remove this line.
    base_url = 'http://127.0.0.1:5000/'

    def check_task_status(task_id: str):
        check_url = f'{base_url}check-status/{task_id}'
        while True:
            response = requests.get(check_url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    if data.get('status') == 'completed':
                        return data
                    elif data.get('status') == 'error':
                        print(f"Error processing task {task_id}: {data.get('message')}")
                        return None
                except requests.exceptions.JSONDecodeError:
                    print(f"Non-JSON response received: {response.text}")
                    return None
            else:
                print(f"Failed to check task status. Status code: {response.status_code}")
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




                    # Construct the 'files' dictionary to send as multipart/form-data
                    files = {
                        'hFileContent': (h_file_name, h_file_content),
                        'cppFileContent': (file_name, cpp_file_content)
                    }



                    print(f"JSON payload: {json.dumps(files)}")

                    response = requests.post(request_url, files=files)

                    if response.status_code == 200:
                        try:
                            print(f"response: {response}")
                            data = response.json()
                            if data.get('status') == 'processing':
                                print(f"Processing started for {file_name}. Task ID: {data.get('id')}")
                                task_result = check_task_status(data.get('id'))
                                if task_result:
                                    print(f"Task completed. Results: {task_result}")
                            else:
                                print(f"Error: {data.get('message')}")
                        except requests.exceptions.JSONDecodeError:
                            print(f"Non-JSON response received: {response.text}")
                    else:
                        print(f"Failed to submit files. Status code: {response.status_code}")
            else:
                print(f"Matching .h file not found for {file_name}")