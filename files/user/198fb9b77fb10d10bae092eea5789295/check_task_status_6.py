# filename: check_task_status.py
from skills import check_task_id_status

# Task ID to check
task_id = "e2099190-7369-4091-8d42-0c500aadf470"

# Call the function to check the task status
status = check_task_id_status(task_id)
print(status)