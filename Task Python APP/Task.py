import os

def clear_screen():
    # For Unix/Linux/Mac OS
    # os.system('clear')
    # For Windows
    os.system('cls')

def show_menu():
    print("Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = " (Completed)" if task["completed"] else ""
            print(f"{i}. {task['task']}{status}")

def mark_completed(tasks):
    view_tasks(tasks)
    index = int(input("Enter the index of the task to mark as completed: ")) - 1
    tasks[index]["completed"] = True
    print("Task marked as completed.")

def delete_task(tasks):
    view_tasks(tasks)
    index = int(input("Enter the index of the task to delete: ")) - 1
    del tasks[index]
    print("Task deleted successfully.")

def main():
    tasks = []
    while True:
        clear_screen()
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")
        input("Press Enter to continue...")
        clear_screen()

if __name__ == "__main__":
    main()