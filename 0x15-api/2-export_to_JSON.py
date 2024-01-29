#!/usr/bin/python3
"""
Script that, using a given REST API, for a given employee ID,
returns information about his/her TODO list progress.
Exports data to JSON format.
"""

import json
from sys import argv
import requests

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

    # Create JSON file
    json_file_name = "{}.json".format(employee_id)

    # Prepare JSON data
    json_data = {
        employee_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_name
            } for task in todo_data
        ]
    }

    # Write JSON data to file
    with open(json_file_name, mode="w") as json_file:
        json.dump(json_data, json_file)

    print("JSON file '{}' has been created.".format(json_file_name))

    # Check if all tasks are present in the JSON file
    if len(todo_data) == len(json_data[employee_id]):
        print("All tasks found: OK")
    else:
        print("Number of tasks missing: {}".format(len(todo_data) - len(json_data[employee_id])))
