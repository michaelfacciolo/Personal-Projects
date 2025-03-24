def display_menu():
    """Display the menu options."""
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. View Completed Tasks")
    print("5. Exit")

def view_tasks(tasks):
    """Display the current tasks in the to-do list."""
    print("\nYour To-Do List:")
    if not tasks:
        print("No pending tasks. Add some!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def view_completed_tasks(completed_tasks):
    """Display the completed tasks."""
    print("\nCompleted Tasks:")
    if not completed_tasks:
        print("No completed tasks yet.")
    else:
        for i, task in enumerate(completed_tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task to the to-do list."""
    task = input("\nEnter the task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added!")
    else:
        print("Task cannot be empty!")

def complete_task(tasks, completed_tasks):
    """Mark a task as completed."""
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to mark as completed: "))
            if 1 <= task_num <= len(tasks):
                completed_task = tasks.pop(task_num - 1)
                completed_tasks.append(completed_task)
                print(f"Task '{completed_task}' marked as completed!")
                print("Nice job! Keep it up!")
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input! Enter a valid task number.")

def main():
    tasks = []
    completed_tasks = []
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks, completed_tasks)
        elif choice == '4':
            view_completed_tasks(completed_tasks)
        elif choice == '5':
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice! Enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
