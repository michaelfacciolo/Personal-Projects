import json
import os
import signal
import sys

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from a file (if it exists) or initialize empty lists."""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as file:
                data = json.load(file)
                return data.get("tasks", []), data.get("completed_tasks", [])
        except (json.JSONDecodeError, IOError):
            print("⚠️ Error loading tasks. Resetting task lists.")
    return [], []  # Default empty lists if file does not exist or is corrupted

def save_tasks(tasks, completed_tasks):
    """Save tasks and completed tasks to a file."""
    try:
        with open(TASKS_FILE, "w") as file:
            json.dump({"tasks": tasks, "completed_tasks": completed_tasks}, file, indent=4)
    except IOError:
        print("⚠️ Error saving tasks. Data might be lost.")

def display_menu():
    """Display the menu options."""
    print("\n📌 To-Do List Menu:")
    print("1️⃣ View To-Do List")
    print("2️⃣ Add Task")
    print("3️⃣ Complete Task")
    print("4️⃣ View Completed Tasks")
    print("5️⃣ Exit")

def view_tasks(tasks):
    """Display the current tasks in the to-do list."""
    print("\n📋 Your To-Do List:")
    if not tasks:
        print("✅ No pending tasks! You're all caught up!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"🔹 {i}. {task}")

def view_completed_tasks(completed_tasks):
    """Display completed tasks."""
    print("\n🏆 Completed Tasks:")
    if not completed_tasks:
        print("😞 No completed tasks yet. Keep going!")
    else:
        for i, task in enumerate(completed_tasks, 1):
            print(f"✅ {i}. {task}")

def add_task(tasks):
    """Add a new task to the to-do list."""
    task = input("\n➕ Enter the task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks, completed_tasks)
        print(f"🎯 Task '{task}' added successfully!")
    else:
        print("⚠️ Task cannot be empty! Please enter a valid task.")

def complete_task(tasks, completed_tasks):
    """Mark a task as completed."""
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\n✔️ Enter the task number to mark as completed: "))
            if 1 <= task_num <= len(tasks):
                completed_task = tasks.pop(task_num - 1)
                completed_tasks.append(completed_task)
                save_tasks(tasks, completed_tasks)
                print(f"🎉 Task '{completed_task}' completed! Keep up the great work!")
            else:
                print("⚠️ Invalid task number. Please try again.")
        except ValueError:
            print("❌ Invalid input! Enter a valid **task number**.")

def exit_program():
    """Handle exit cleanly."""
    print("\n👋 Exiting the To-Do List. See you next time!")
    sys.exit(0)

def main():
    """Main function to run the to-do list program."""
    global tasks, completed_tasks
    tasks, completed_tasks = load_tasks()

    while True:
        display_menu()
        choice = input("\n🔢 Enter your choice (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks, completed_tasks)
        elif choice == "4":
            view_completed_tasks(completed_tasks)
        elif choice == "5":
            exit_program()
        else:
            print("❌ Invalid choice! Enter a number between **1 and 5**.")

if __name__ == "__main__":
    # Handle Ctrl+C gracefully
    signal.signal(signal.SIGINT, lambda sig, frame: exit_program())
    main()
