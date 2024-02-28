# filename: check_task_status.py

from skills import check_task_id_status

# The task ID to check
task_id = "d4579a89-0a5f-4c9f-8a0e-5ada82de397f"

# Call the function to check the task status
status = check_task_id_status(task_id)
print(status)