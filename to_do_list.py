# to_do_list.py

def display_menu():
    print("\nTo-Do List Menu")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")


def view_tasks(tasks):
    print("\nYour Tasks:")
    if not tasks:
        print("No tasks found!")
    else:
        for idx, (task, done) in enumerate(tasks.items(), start=1):
            status = "✓" if done else "✗"
            print(f"{idx}. [{status}] {task}")


def add_task(tasks):
    task = input("Enter the task: ").strip()
    if task:
        tasks[task] = False
        print(f"Task '{task}' added successfully!")
    else:
        print("Task cannot be empty!")


def mark_task_done(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as done: "))
        task_name = list(tasks.keys())[task_num - 1]
        tasks[task_name] = True
        print(f"Task '{task_name}' marked as done!")
    except (ValueError, IndexError):
        print("Invalid task number!")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        task_name = list(tasks.keys())[task_num - 1]
        del tasks[task_name]
        print(f"Task '{task_name}' deleted successfully!")
    except (ValueError, IndexError):
        print("Invalid task number!")


def main():
    tasks = {}  # Dictionary to store tasks and their status (True for done, False for pending)
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                view_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                mark_task_done(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                print("Exiting To-Do List. Goodbye!")
                break
            else:
                print("Invalid choice! Please choose between 1-5.")
        except ValueError:
            print("Please enter a valid number!")


if __name__ == "__main__":
    main()
