# filename: create_unit_tests.py
import os

def create_unit_tests(parent_dir: str, uut_dir: str = 'UUT', src_dir: str = 'src'):
    uut_path = os.path.join(parent_dir, uut_dir)
    src_path = os.path.join(parent_dir, src_dir)

    # Ensure both UUT and src directories exist
    for path in [uut_path, src_path]:
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Directory '{path}' was created.")
        else:
            print(f"Directory '{path}' already exists.")
    
    # List C++ files for which to create unit tests
    for file_name in os.listdir(uut_path):
        if file_name.endswith('.cpp'):
            print(f"Found C++ file for unit testing: {file_name}")
            # Here you would add the logic to generate unit tests using a specific framework

# Change this to the path where you want to create unit tests
parent_directory = '/home/wilsonb/dl/github.com/BruceRayWilson/Accounting'
create_unit_tests(parent_directory)