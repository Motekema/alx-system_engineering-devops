#!/usr/bin/python3
"""
Script that, using a given REST API, for a given employee ID,
returns information about his/her TODO list progress.
Exports data to CSV format.
"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = argv[1]

    # Fetch user data
    user_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    )
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch TODO list data
    todo_response = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".
        format(employee_id)
    )
    todo_data = todo_response.json()

    # Create CSV file
    csv_file_name = "{}.csv".format(employee_id)

    with open(csv_file_name, mode="w", newline="") as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", 
                "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write CSV header
        writer.writeheader()

        # Write tasks data to CSV
        for task in todo_data:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": str(task.get("completed")),
                "TASK_TITLE": task.get("title")
            })

    print("CSV file '{}' has been created.".format(csv_file_name))

