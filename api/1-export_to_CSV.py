#!/usr/bin/python3
import requests
import sys
import csv

def export_employee_todo_to_csv(employee_id):
    # Fetching the employee details
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error: Employee not found.")
        return
    employee_data = user_response.json()
    employee_name = employee_data.get('name', 'Unknown')
    employee_username = employee_data.get('username', 'Unknown')

    # Fetching the employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error: Unable to fetch TODO list.")
        return
    todos = todos_response.json()

    # Defining the CSV file name
    csv_filename = f"{employee_id}.csv"

    # Writing to CSV file
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos:
            writer.writerow([
                employee_id,
                employee_username,
                task['completed'],
                task['title']
            ])

    print(f"Data exported to {csv_filename} successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        export_employee_todo_to_csv(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
