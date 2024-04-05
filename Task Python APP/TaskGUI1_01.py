import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        task_entry.delete(0, tk.END)
        messagebox.showinfo("Task Added", "Task added successfully!")
    else:
        messagebox.showwarning("Empty Task", "Please enter a task.")

def view_tasks():
    if not tasks:
        messagebox.showinfo("No Tasks", "No tasks yet.")
    else:
        tasks_text = "\n".join([f"{i+1}. {task['task']}" + (" (Completed)" if task['completed'] else "") for i, task in enumerate(tasks)])
        messagebox.showinfo("Tasks", tasks_text)

def mark_completed():
    index_text = index_entry.get()
    if index_text.isdigit():
        index = int(index_text) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            messagebox.showinfo("Task Completed", "Task marked as completed.")
        else:
            messagebox.showwarning("Invalid Index", "Please enter a valid index.")
    else:
        messagebox.showwarning("Invalid Input", "Please enter a valid index.")

def delete_task():
    index_text = index_entry.get()
    if index_text.isdigit():
        index = int(index_text) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            messagebox.showinfo("Task Deleted", "Task deleted successfully.")
        else:
            messagebox.showwarning("Invalid Index", "Please enter a valid index.")
    else:
        messagebox.showwarning("Invalid Input", "Please enter a valid index.")

def clear_entry(event):
    index_entry.delete(0, tk.END)

def show_menu():
    menu_window = tk.Tk()
    menu_window.title("Task List App")

    global task_entry
    task_entry = tk.Entry(menu_window)
    task_entry.pack(side=tk.LEFT)

    add_button = tk.Button(menu_window, text="Add Task", command=add_task)
    add_button.pack(side=tk.LEFT)

    view_button = tk.Button(menu_window, text="View Tasks", command=view_tasks)
    view_button.pack()

    mark_button = tk.Button(menu_window, text="Mark Task as Completed", command=mark_completed)
    mark_button.pack()

    delete_button = tk.Button(menu_window, text="Delete Task", command=delete_task)
    delete_button.pack()

    global index_entry
    index_entry = tk.Entry(menu_window)
    index_entry.pack()
    index_entry.insert(0, "Enter index")
    index_entry.bind("<FocusIn>", clear_entry)

    menu_window.mainloop()

if __name__ == "__main__":
    tasks = []
    show_menu()
