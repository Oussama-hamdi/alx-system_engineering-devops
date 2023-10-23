#!/usr/bin/python3
"""Returns information about employee TODO list progress to a JSON file"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as json_file:
        json.dump({
            user.get("id"): [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            } for task in requests.get(url + "todos",
                                       params={"userId": user.get("id")})
                                       .json()] for user in users}, json_file)
