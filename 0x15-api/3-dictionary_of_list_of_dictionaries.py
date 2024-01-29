#!/usr/bin/python3
"""
Script that, using a given REST API, retrieves information
about all employee TODO lists.
Exports data to JSON format.
"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    resp = requests.get(url)
    Users = resp.json()

    users_dict = {}
    for user in Users:
        USER_ID = user.get('id')
        USERNAME = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID)
        url = url + '/todos/'
        resp = requests.get(url)

        tasks = resp.json()
        users_dict[USER_ID] = []
        for task in tasks:
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            users_dict[USER_ID].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME
            })
            """little Something"""
    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f)
