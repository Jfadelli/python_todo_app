import tkinter as tk

# Dummy data representing tasks
tasks = {
    1: {"task": "Buy groceries", "completed": False},
    2: {"task": "Clean the house", "completed": False},
    3: {"task": "Walk the dog", "completed": True},
}

# Function to remove a task


def remove_task(task_id):
    del tasks[task_id]
    update_task_list()

# Function to mark a task as complete


def mark_complete(task_id):
    tasks[task_id]["completed"] = True
    update_task_list()

# Function to update the task list display


def update_task_list():
    for widget in task_list_frame.winfo_children():
        widget.destroy()
    for widget in completed_task_list_frame.winfo_children():
        widget.destroy()

    # Display active tasks
    for task_id, task_info in tasks.items():
        task_text = task_info["task"]
        task_completed = task_info["completed"]

        task_frame = tk.Frame(task_list_frame if not task_completed else completed_task_list_frame,
                              bg="#FFEB3B" if not task_completed else "#90EE90", pady=5)
        task_frame.pack(fill="x", pady=5)

        task_label = tk.Label(task_frame, text=task_text, fg="black",
                              bg="#FFEB3B" if not task_completed else "#90EE90")
        task_label.pack(side="left", padx=5)

        # Add a remove button (red X)
        remove_button = tk.Button(task_frame, text="❌", bg="red", fg="white",
                                  command=lambda task_id=task_id: remove_task(task_id))
        remove_button.pack(side="right", padx=5)

        # Add a mark complete button (green checkmark) if not completed
        if not task_completed:
            complete_button = tk.Button(task_frame, text="✔️", bg="green",
                                        fg="white", command=lambda task_id=task_id: mark_complete(task_id))
            complete_button.pack(side="right", padx=5)


# Create GUI elements
root = tk.Tk()
root.title("To Do App")
root.configure(bg='#2E2E2E')  # Dark gray background color using hex code
root.geometry("500x400")

# Title label with hex color
# White text on dark gray background
label_title = tk.Label(root, text="To Do List", bg="#2E2E2E", fg="#FFFFFF")
label_title.pack(pady=10)

# Frame to hold the input field and the button side by side
frame = tk.Frame(root, bg='#1C1C1C')  # Darker background for the main frame
frame.pack(fill="x", pady=10)

# Task input field frame (80% width)
# White background for the input field frame
task_entry_frame = tk.Frame(frame, bg='#FFFFFF')
task_entry_frame.pack(side="left", fill="x", expand=True)

task_entry = tk.Entry(task_entry_frame, width=35)
task_entry.pack(fill="x", padx=5, pady=5)

# Task list frame (for incomplete tasks)
task_list_label = tk.Label(root, text="To Do", bg="#2E2E2E", fg="#FFFFFF")
task_list_label.pack()
# Yellow background for the task list frame
task_list_frame = tk.Frame(root, bg='#FFEB3B')
task_list_frame.pack(fill="x", pady=5, padx=10)

# Completed task list frame
task_completed_label = tk.Label(
    root, text="Completed Tasks", bg="#2E2E2E", fg="#FFFFFF")
task_completed_label.pack()
# Light green background for completed tasks
completed_task_list_frame = tk.Frame(root, bg='#90EE90')
completed_task_list_frame.pack(fill="x", pady=5, padx=10)

# Initial render of tasks
update_task_list()

root.mainloop()
