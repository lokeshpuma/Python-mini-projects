def task():
    task = []
    print("--WELCOME TO THE TASK MANAGER--")

    total_tasks = int(input("Enter the number of tasks you want to add: "))

    for i in range(total_tasks+1):
        task_name = input(f"Enter the name of task {i+1}: ")
        task.append(task_name)

    print(f"Today's Tasks: {task}")

    while True:
        operation = input("Do you want to add,update,remove,view or exit a task? (add/remove/exit): ").strip().lower()
        if operation == 'add':
            add = input("Enter the task you want to add: ")
            task.append(add)
            print(f"Today's Tasks: {task} added successfully.")

        elif operation == 'remove':
            remove = input("Enter the task you want to remove: ")
            if remove in task:
                task.remove(remove)
                print(f"Today's Tasks: {task} removed successfully.")
            else:
                print("Task not found.")

        elif operation == 'view':
            print(f"Today's Tasks: {task}")

        elif operation == 'update':
            update = input("Enter the task you want to update: ")
            if update in task:
                index = task.index(update)
                new_task = input("Enter the new task: ")
                task[index] = new_task
                print(f"Today's Tasks: {task} updated successfully.")
            else:
                print("Task not found.")    



task()