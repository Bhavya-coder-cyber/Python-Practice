import os
TASK_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if(os.path.exists(TASK_FILE)):
        with open(TASK_FILE, "r") as f:
            for line in f:
                text, status = line.strip().rsplit("||", 1)
                tasks.append({"text": text, "status": status == "done"})
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            status = "done" if task["done"] else "not done"
            f.write(f"{task['text']}||{status}\n")

def display_task(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            completed = "✅" if task["done"] else " "
            print(f"{i}. {completed} {task['text']}")
    print()

def tasklist_manager():
    tasks = load_tasks()
    while True:
        print("\n------Task List Manager-------\n")
        print("1. Add Task")
        print("2. View Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()
        
        match choice:
            case "1":
                task = input("Enter the task: ").strip()
                if task:
                    tasks.append({"text": task, "done": False})
                    save_tasks(tasks)
                    print("Task added successfully.")
                else:
                    print("Task cannot be empty.")
            case "2":
                display_task(tasks)
            case "3":
                display_task(tasks)
                try:
                    task_index = int(input("Enter the task number to mark as done: ").strip())
                    if 1 <= task_index <= len(tasks):
                        tasks[task_index - 1]["done"] = True
                        save_tasks(tasks)
                        print("Task marked as done.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            case "4":
                display_task(tasks)
                try:
                    task_index = int(input("Enter the task number to delete: ").strip())
                    if 1 <= task_index <= len(tasks):
                        removed = tasks.pop(task_index - 1)
                        save_tasks(tasks)
                        print("Task deleted Successfully.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            case "5":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")
                
tasklist_manager()
