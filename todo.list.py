import json
import os

FILE_NAME = "todo_list.json"

# Load tasks from JSON file
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

# Save tasks to JSON file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(task_name):
    tasks = load_tasks()
    task = {"task": task_name, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task '{task_name}' added successfully!")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return
    print("\n📝 To-Do List:")
    for index, task in enumerate(tasks, start=1):
        status = "✅ Done" if task["completed"] else "❌ Not Done"
        print(f"{index}. {task['task']} - {status}")

# Mark a task as completed
def mark_task_done(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1]["completed"] = True
        save_tasks(tasks)
        print(f"🎯 Task '{tasks[index - 1]['task']}' marked as completed!")
    else:
        print("⚠️ Invalid task number. Please try again.")

# Delete a task
def delete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Task '{removed_task['task']}' deleted successfully!")
    else:
        print("⚠️ Task not found. Please enter a valid number.")

# Main menu
def main():
    while True:
        print("\n===== 🧾 TO-DO LIST MENU =====")
        print("1️⃣ Add Task")
        print("2️⃣ View Tasks")
        print("3️⃣ Mark Task as Done")
        print("4️⃣ Delete Task")
        print("5️⃣ Exit")

        choice = input("👉 Enter your choice (1-5): ")

        if choice == "1":
            task_name = input("✍️ Enter task name: ")
            add_task(task_name)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                index = int(input("Enter task number to mark as done: "))
                mark_task_done(index)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == "4":
            view_tasks()
            try:
                index = int(input("Enter task number to delete: "))
                delete_task(index)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == "5":
            print("👋 Exiting the program. Have a productive day!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
