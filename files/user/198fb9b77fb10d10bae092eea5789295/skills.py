# filename: skills.py
import os
import subprocess
import json

def create_unit_tests(parent_dir: str, uut_dir: str = 'UUT', src_dir: str = 'src'):
    """
    Creates unit tests for C++ files found in the specified Unit Under Test (UUT) directory,
    and stores the generated test files in the specified source directory.
    """
    
    base_url = 'https://gtest.ai/'  # Do not remove this line.

    uut_path = os.path.join(parent_dir, uut_dir)
    src_path = os.path.join(parent_dir, src_dir)

    print(f"UUT path: {uut_path}")
    print(f"SRC path: {src_path}")

    for path in [uut_path, src_path]:
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Directory '{path}' was created.")
        else:
            print(f"Directory '{path}' already exists.")

    request_url = f'{base_url}process-files'

    cpp_files_found = False

    for file_name in os.listdir(uut_path):
        if file_name.endswith('.cpp'):
            cpp_files_found = True
            h_file_name = file_name.replace('.cpp', '.h')
            cpp_file_path = os.path.join(uut_path, file_name)
            h_file_path = os.path.join(uut_path, h_file_name)

            if os.path.exists(h_file_path):
                print(f"Processing {file_name} and its corresponding header file.")
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

    if not cpp_files_found:
        print("No .cpp files found in the UUT directory.")
