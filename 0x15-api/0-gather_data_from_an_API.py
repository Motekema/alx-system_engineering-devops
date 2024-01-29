#!/usr/bin/python3
"""
Script that, using a given REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

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

    # Calculate progress
    total_tasks = len(todo_data)
    done_tasks = sum(task.get("completed") for task in todo_data)

    # Display information
    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, done_tasks, total_tasks
        )
    )

    for task in todo_data:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))
