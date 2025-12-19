"""
Question 3: File Handling & Modules (25 Marks | 45 Minutes)

Objective: Test file operations and modular coding.

Problem Statement: Create a Task Logger Application.

Requirements=
Take user input:
Task name
Task status (Completed / Pending)
Save tasks into a JSON file
Read the JSON file and display all saved tasks

Use:
with open()
json module
Organize logic using functions
"""


import json


# ------------------------------
# Read json task file
# ------------------------------
def load_task():
    try:
        with open("Logger_Application.json", 'r') as file:
            return json.load(file)
    except FileNotFoundError as e:
        print(e)
        return []
    
# ------------------------------
# save json task
# ------------------------------
def save_task(tasks):
    try:
        with open("Logger_Application.json", "w") as file:
            return json.dump(tasks, file, indent=4)
    except FileNotFoundError as e:
        print(e)
        return 

# ------------------------------
# add new task in json file
# ------------------------------
def add_task():
    task_name = input("Enter task name: ").title()
    status = input("Enter task status completed or pending: ").title()

    if status not in ['Completed', 'Pending']:
        print("Invalid status!, Task not saved.")
        return
    
    task = {
        "Task_Name": task_name,
        "Task_Status" : status
    }

    tasks = load_task()
    tasks.append(task)
    save_task(tasks)


# ------------------------------
# show json task
# ------------------------------
def show_task():
    tasks = load_task()

    if not tasks:
        print("No task found.")
        return
    else: 
        print("\n*****Task List*****")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t['Task_Name']} - {t['Task_Status']}")





# ------------------------

while True:
    print("\n******** Logger Application ********")
    print("1. Add task")
    print("2. View task")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice(1/2/3): "))
    except ValueError:
        print("Invalid input! Please Enter (1/2/3) number.")
        continue

    if choice == 1:
        add_task()
    elif choice == 2:
        show_task()
    elif choice == 3:
        print("Thank you!")
        break
    else:
        print("Invalid Choice!")
