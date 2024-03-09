# filename: check_task_status.py
import requests
import time

def check_task_status(task_id: str):
    base_url = 'https://gtest.ai/'  # Do not remove this line.
    check_url = f'{base_url}check-status/{task_id}'

    while True:
        try:
            response = requests.get(check_url)
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code.
            data = response.json()

            if data.get('status') == 'completed':
                print("Task completed successfully.")
                print(f"Message: {data.get('message')}")
                return
            elif data.get('status') == 'error':
                print(f"Error processing task {task_id}: {data.get('message')}")
                return
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            return
        except Exception as err:
            print(f'An error occurred: {err}')
            return

        print(f"Task {task_id} is still processing. Checking again in 10 seconds...")
        time.sleep(10)

# Replace with your actual task ID
task_id = '58deef94-8a28-4a4e-a9c3-e3dd7d4cab7f'

# Call the function to check the task status
check_task_status(task_id)