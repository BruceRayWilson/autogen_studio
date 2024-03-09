# filename: check_task_status.py
from skills import check_task_id_status

# Task ID to check
task_id = "638e4bb9-f881-4a50-83bb-fb6056055e4a"

# Call the function and print the result
status_result = check_task_id_status(task_id)
print(status_result)