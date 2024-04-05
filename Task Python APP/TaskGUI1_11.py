import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "completed": False, "completion_date": ""})
        task_entry.delete(0, tk.END)
        update_tasks_listbox()
        save_tasks()
        messagebox.showinfo("Task Added", "Task added successfully!")
    else:
        messagebox.showwarning("Empty Task", "Please enter a task.")

def update_tasks_listbox():
    tasks_listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        if task["completed"]:
            status = f"(Completed on {task['completion_date']})"
        else:
            status = ""
        tasks_listbox.insert(tk.END, f"{i+1}. {task['task']} {status}")

def mark_completed():
    selected_index = tasks_listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        tasks[index]["completed"] = True
        tasks[index]["completion_date"] = datetime.now().strftime("%Y-%m-%d")
        update_tasks_listbox()
        save_tasks()
        messagebox.showinfo("Task Completed", "Task marked as completed.")
    else:
        messagebox.showwarning("No Task Selected", "Please select a task to mark as completed.")

def delete_task():
    selected_index = tasks_listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        del tasks[index]
        update_tasks_listbox()
        save_tasks()
        messagebox.showinfo("Task Deleted", "Task deleted successfully.")
    else:
        messagebox.showwarning("No Task Selected", "Please select a task to delete.")

def show_menu():
    menu_window = tk.Tk()
    menu_window.title("Nethergear Task App Version 1.11")

    global task_entry
    task_entry_label = tk.Label(menu_window, text="Please enter a new task:")
    task_entry_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    task_entry = tk.Entry(menu_window)
    task_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    add_button = tk.Button(menu_window, text="Add Task", command=add_task)
    add_button.grid(row=0, column=2, padx=5, pady=5, sticky="ewns")

    global tasks_listbox
    tasks_listbox = tk.Listbox(menu_window, width=50, height=10)
    tasks_listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

    mark_button = tk.Button(menu_window, text="Mark Task as Completed", command=mark_completed)
    mark_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

    delete_button = tk.Button(menu_window, text="Delete Task", command=delete_task)
    delete_button.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

    menu_window.rowconfigure(1, weight=1)
    menu_window.columnconfigure((0, 1, 2), weight=1)

    # Load image and scale down
    img = tk.PhotoImage(file="Nethergear.png")
    img = img.subsample(10)  # Scale down the image

    # Add image label spanning rows 3 to 6
    img_label = tk.Label(menu_window, image=img)
    img_label.image = img
    img_label.grid(row=3, column=0, rowspan=9, padx=5, pady=0, sticky="w")

    # Add text label
    text_label = tk.Label(menu_window, text=" ")
    text_label.grid(row=3, column=1, padx=0, pady=0, sticky="w")
    text_label = tk.Label(menu_window, text=" ")
    text_label.grid(row=4, column=1, padx=0, pady=0, sticky="w")    
    text_label = tk.Label(menu_window, text="Nethergear Task Application Version 1.11")
    text_label.grid(row=5, column=1, padx=0, pady=0, sticky="w")
    text_label = tk.Label(menu_window, text="A simple Python task management application")
    text_label.grid(row=6, column=1, padx=0, pady=0, sticky="w")
    text_label = tk.Label(menu_window, text="Created by Jasper Houtman")
    text_label.grid(row=7, column=1, padx=0, pady=0, sticky="w")
    text_label = tk.Label(menu_window, text="App created on the 17th of Februari 2024")
    text_label.grid(row=8, column=1, padx=0, pady=0, sticky="w")
    text_label = tk.Label(menu_window, text="Current version date is the 18th of februari 2024")
    text_label.grid(row=9, column=1, padx=0, pady=0, sticky="w")
    text_label = tk.Label(menu_window, text=" ")
    text_label.grid(row=10, column=1, padx=0, pady=0, sticky="w")
    text_label = tk.Label(menu_window, text=" ")
    text_label.grid(row=11, column=1, padx=0, pady=0, sticky="w")


    tasks.extend(load_tasks())
    update_tasks_listbox()

    menu_window.mainloop()

if __name__ == "__main__":
    tasks = []
    show_menu()
