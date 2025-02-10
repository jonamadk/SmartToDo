import json
import os

# Store tasks.json in a volume-mounted directory
tasks_file = "/app/data/tasks.json"

def load_tasks():
    # Check if the tasks file exists in the mounted volume
    if os.path.exists(tasks_file):
        with open(tasks_file, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    # Save tasks to the volume-mounted tasks.json
    with open(tasks_file, "w") as file:
        json.dump(tasks, file, indent=4)

def get_next_task_id(tasks):
    task_ids = [task.get("task_id", 0) for task in tasks]
    return max(task_ids, default=0) + 1

def add_task():
    title = input("Enter title: ")
    description = input("Enter description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks = load_tasks()
    task_id = get_next_task_id(tasks)
    tasks.append({"task_id": task_id, "title": title, "description": description, "due_date": due_date, "done": False})
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        status = "Done" if task["done"] else "Pending"
        print(f"{task['task_id']}. {task['title']} - {task['description']} - Due: {task['due_date']} - Status: {status}")

def mark_task_done():
    tasks = load_tasks()
    view_tasks()
    task_num = int(input("Enter task ID to mark as done: "))
    for task in tasks:
        if task["task_id"] == task_num:
            task["done"] = True
            save_tasks(tasks)
            print("Task marked as done!")
            return
    print("Invalid task ID.")

def delete_task():
    tasks = load_tasks()
    view_tasks()
    task_num = int(input("Enter task ID to delete: "))
    tasks = [task for task in tasks if task["task_id"] != task_num]
    save_tasks(tasks)
    print("Task deleted successfully!")

def main():
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Done\n4. Delete Task\n5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
