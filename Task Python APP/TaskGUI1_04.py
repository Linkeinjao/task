import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        task_entry.delete(0, tk.END)
        update_tasks_listbox()
        messagebox.showinfo("Task Added", "Task added successfully!")
    else:
        messagebox.showwarning("Empty Task", "Please enter a task.")

def update_tasks_listbox():
    tasks_listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "(Completed)" if task["completed"] else ""
        tasks_listbox.insert(tk.END, f"{i+1}. {task['task']} {status}")

def mark_completed():
    selected_index = tasks_listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        tasks[index]["completed"] = True
        update_tasks_listbox()
        messagebox.showinfo("Task Completed", "Task marked as completed.")
    else:
        messagebox.showwarning("No Task Selected", "Please select a task to mark as completed.")

def delete_task():
    selected_index = tasks_listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        del tasks[index]
        update_tasks_listbox()
        messagebox.showinfo("Task Deleted", "Task deleted successfully.")
    else:
        messagebox.showwarning("No Task Selected", "Please select a task to delete.")

def show_menu():
    menu_window = tk.Tk()
    menu_window.title("Task List App")

    global task_entry
    task_entry = tk.Entry(menu_window)
    task_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

    add_button = tk.Button(menu_window, text="Add Task", command=add_task)
    add_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    global tasks_listbox
    tasks_listbox = tk.Listbox(menu_window, width=50, height=10)
    tasks_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    mark_button = tk.Button(menu_window, text="Mark Task as Completed", command=mark_completed)
    mark_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

    delete_button = tk.Button(menu_window, text="Delete Task", command=delete_task)
    delete_button.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

    menu_window.rowconfigure(1, weight=1)
    menu_window.columnconfigure((0, 1), weight=1)

    menu_window.mainloop()

if __name__ == "__main__":
    tasks = []
    show_menu()
