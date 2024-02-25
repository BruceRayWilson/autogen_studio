# filename: create_unit_tests.py
import os

def create_unit_tests(parent_dir: str, uut_dir: str = 'UUT', src_dir: str = 'src'):
    """
    Simulates the creation of unit tests for C++ files found in the specified Unit Under Test (UUT) directory,
    and stores the generated test files in the specified source directory.
    """
    uut_path = os.path.join(parent_dir, uut_dir)
    src_path = os.path.join(parent_dir, src_dir)

    # Ensure both UUT and src directories exist
    for path in [uut_path, src_path]:
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Directory '{path}' was created.")
        else:
            print(f"Directory '{path}' already exists.")
    
    # Simulate test creation for each C++ file
    for file_name in os.listdir(uut_path):
        if file_name.endswith('.cpp'):
            h_file_name = file_name.replace('.cpp', '.h')
            test_file_name = file_name.replace('.cpp', '_test.cpp')
            test_file_path = os.path.join(src_path, test_file_name)
            
            # Check for the existence of the corresponding header file
            h_file_path = os.path.join(uut_path, h_file_name)
            if os.path.exists(h_file_path):
                # Simulate test file creation
                with open(test_file_path, 'w') as test_file:
                    test_file_content = f"// Unit tests for {file_name}\n"
                    test_file.write(test_file_content)
                print(f"Test file '{test_file_name}' created for '{file_name}'.")
            else:
                print(f"Matching header file not found for '{file_name}'. No test file created.")

# Usage
create_unit_tests("/home/wilsonb/dl/github.com/BruceRayWilson/Accounting")