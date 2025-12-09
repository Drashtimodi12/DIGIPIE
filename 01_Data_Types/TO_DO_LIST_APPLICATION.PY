tasks = []
print("\n=========WELCOME=========")

def display_menu():
    print("\n============Task Meanu============")
    print("1. Add Task.")
    print("2. Edit Task.")
    print("3. Delete Task.")
    print("4. Exit.")


while True:
    display_menu()

    try:
        choice = int(input("Select option to do task: "))

        # -------------------------------Add-----------------------------------
        if choice == 1:
            print("===ADDING TODAY WORK===")
            add = input("Enter your today work task: ").title()

            tasks.append(add)
            print("Task added successfully!")


        # -------------------------------edit-----------------------------------
        elif choice == 2:
            print("===EDIT TODAY WORK===")
            if len(tasks) == 0:
                print("Task list is empty!")
            else:
                print("Your Whole task list is: ")
                for indexes, task in enumerate(tasks):
                    print(f"{indexes+1}. {task}")

                task_id = int(input("Enter task index to edit: "))-1

                if 0 <= task_id < len(tasks):
                    new_task = input("Enter new task: ").title()
                    tasks[task_id] = new_task
                    print("Task edited successfully!")
                else:
                    print("Invalid task id.")     

        # -------------------------------Delete-----------------------------------
        elif choice == 3:
            print("===DELETE TODAY WORK===")
            if len(tasks)== 0:
                print("Task list is empty!")
            else:
                print(f"Your Whole task list is:")
                for indexes, task in enumerate(tasks):
                    print(f"{indexes+1}. {task}")

                task_id = int(input("Enter task index to delete: "))-1

                if 0 <= task_id < len(tasks):
                    tasks.pop(task_id)
                    print("Task deleted successfully!")
                else: 
                    print("Invalid task id.")

        elif choice == 4:
            print("Exiting the application!")
            break
        else:
            print("Invalid choice. Please Enter a valid option.")

    except Exception as e:
        print("Error Occured: ", e)






