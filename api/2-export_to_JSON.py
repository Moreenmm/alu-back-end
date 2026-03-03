#!/usr/bin/python3
import requests
import sys
import json

def export_employee_todo_to_json(employee_id):
    # Fetching employee details
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error: Employee not found.")
        return
    employee_data = user_response.json()
    employee_username = employee_data.get('username', 'Unknown')

    # Fetching employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error: Unable to fetch TODO list.")
        return
    todos = todos_response.json()

    # Preparing JSON data
    json_data = {
        str(employee_id): [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": employee_username
            }
            for task in todos
        ]
    }

    # Defining JSON file name
    json_filename = f"{employee_id}.json"

    # Writing to JSON file
    with open(json_filename, mode='w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=4)

    print(f"Data exported to {json_filename} successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        export_employee_todo_to_json(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
