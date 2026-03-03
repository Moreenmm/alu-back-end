#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    # Fetch employee details
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error: Employee not found.")
        return
    employee_name = user_response.json().get('name', 'Unknown')

    # Fetching the employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error: Unable to fetch TODO list.")
        return
    todos = todos_response.json()

    # Calculating the progress
    completed_tasks = [task for task in todos if task['completed']]
    total_tasks = len(todos)
    done_tasks = len(completed_tasks)

    # Displaying employees progress
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
