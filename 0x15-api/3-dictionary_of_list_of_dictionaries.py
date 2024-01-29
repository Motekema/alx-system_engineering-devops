#!/usr/bin/python3
"""
Script that, using a given REST API, retrieves information about all employee TODO lists.
Exports data to JSON format.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(argv) != 1:
        print("Usage: {} ".format(argv[0]))
        exit(1)

    # Fetch all users
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    users_data = users_response.json()

    # Create a dictionary to store tasks for each user
    all_tasks = {}
    
    # Fetch tasks for each user
    for user in users_data:
        user_id = str(user.get("id"))
        user_name = user.get("username")

        # Fetch TODO list data for the current user
        todo_response = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}".
            format(user_id)
        )
        todo_data = todo_response.json()

        # Prepare tasks data for the current user
        tasks_data = [
            {
                "username": user_name,
                "task": task.get("title"),
                "completed": task.get("completed"),
            } for task in todo_data
        ]

        # Update the dictionary with tasks data for the current user
        all_tasks[user_id] = tasks_data

    # Create JSON file
    json_file_name = "todo_all_employees.json"

    # Prepare JSON data for all users
    json_data = json.dumps(all_tasks)

    # Write JSON data to file
    with open(json_file_name, mode="w") as json_file:
        json_file.write(json_data)

    print("JSON file '{}' has been created.".format(json_file_name))

