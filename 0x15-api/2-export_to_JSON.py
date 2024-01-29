#!/usr/bin/python3
"""
Script that, using a given REST API, for a given employee ID,
returns information about his/her TODO list progress.
Exports data to JSON format.
"""

import csv
import json
import requests
import sys


if __name__ == '__main__':
    USER_ID = sys.argv[1]
    url_to_user = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    res = requests.get(url_to_user)
    """Documentations"""
    USERNAME = res.json().get('username')
    """Documentations"""
    url_to_task = url_to_user + '/todos'
    res = requests.get(url_to_task)
    tasks = res.json()

    dict_data = {USER_ID: []}
    for task in tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        dict_data[USER_ID].append({
                                  "task": TASK_TITLE,
                                  "completed": TASK_COMPLETED_STATUS,
                                  "username": USERNAME})
    """prints(dict_data)"""
    with open('{}.json'.format(USER_ID), 'w') as f:
        json.dump(dict_data, f)
