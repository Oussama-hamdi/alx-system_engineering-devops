#!/usr/bin/python3
"""Returns information about employee TODO list progress"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todo = requests.get(url + "todos", params={"userId": user_id}).json()
    completed_tasks = [t.get("title") for t in todo if t.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todo)))

    for task in completed_tasks:
        print("\t {}".format(task))
