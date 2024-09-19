import json
from datetime import datetime

# Global variable to store tasks
tasks = []

# Load tasks from file
def load_tasks():
    global tasks
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

# Save tasks to file
def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task():
    name = input("Enter task name: ")
    priority = input("Enter priority (Low, Medium, High): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    try:
        due_date = datetime.strptime(due_date, '%Y-%m-%d').strftime('%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Task not added.")
        return

    task = {
        'name': name,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    }
    tasks.append(task)
    print("Task added successfully!")

# View all tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for idx, task in enumerate(tasks, start=1):
        status = "Completed" if task['completed'] else "Pending"
        print(f"{idx}. {task['name']} - {task['priority']} priority - Due: {task['due_date']} - Status: {status}")

# Mark task as complete
def complete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
            print(f"Task {task_num} marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f"Deleted task: {deleted_task['name']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu
def menu():
    load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            save_tasks()
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if _name_ == "_main_":
    menu()
