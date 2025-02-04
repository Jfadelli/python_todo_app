import tkinter as tk


color_pallete = {
    "old_rose":"#CC8B86",
    "linen":"#F9EAE1",
    "rose_taupe":"#7D4F50",
    "dun":"#D1BE9C",
    "cinerous":"#AA998F",
}
# Dummy data representing tasks
tasks = {
    1: {"task": "Buy groceries", "completed": False},
    2: {"task": "Clean the house", "completed": False},
    3: {"task": "Walk the dog", "completed": True},
}

# Create GUI elements
root = tk.Tk()
root.title("To Do App")
root.configure(bg=color_pallete["rose_taupe"])  # Dark gray background color using hex code
root.geometry("500x400")

# Function to remove a task
def remove_task(task_id):
    del tasks[task_id]
    update_task_list()

# Function to mark a task as complete
def mark_complete(task_id):
    tasks[task_id]["completed"] = True
    update_task_list()

# Function to add a new task
def add_task():
    task_text = task_entry.get().strip()
    if task_text:  # Ensure it's not empty
        new_task_id = max(tasks.keys(), default=0) + 1  # Generate a new ID
        tasks[new_task_id] = {"task": task_text, "completed": False}
        task_entry.delete(0, tk.END)  # Clear the input field
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

        task_frame = tk.Frame(task_list_frame if not task_completed else completed_task_list_frame, bg=color_pallete["old_rose"] if not task_completed else color_pallete["old_rose"], pady=5)
        task_frame.pack(fill="x", pady=5)

        task_label = tk.Label(task_frame, text=task_text, fg="black", bg=color_pallete["old_rose"] if not task_completed else color_pallete["old_rose"])
        task_label.pack(side="left", padx=5)

        # Add a remove button (red X)
        remove_button = tk.Button(task_frame, text="❌", bg="red", fg="white", command=lambda task_id=task_id: remove_task(task_id))
        remove_button.pack(side="right", padx=5)

        # Add a mark complete button (green checkmark) if not completed
        if not task_completed:
            complete_button = tk.Button(task_frame, text="✔️", bg=color_pallete["rose_taupe"], fg="white", command=lambda task_id=task_id: mark_complete(task_id))
            complete_button.pack(side="right", padx=5)

# Title label with hex color
label_title = tk.Label(root, text="To Do App", bg=color_pallete["rose_taupe"], fg=color_pallete["linen"],font=("Arial", 16, "bold"))
label_title.pack(pady=10)

# Frame to hold the input field and the button side by side
frame = tk.Frame(root, bg=color_pallete["linen"])  # Darker background for the main frame
frame.pack(fill="x", pady=10)

# Task input field
task_entry = tk.Entry(frame, width=30)
task_entry.pack(side="left", fill="x", expand=True, padx=5, pady=5)

# Add Task button
add_task_button = tk.Button(frame, text="Add Task", bg=color_pallete["dun"], fg="black", command=add_task)
add_task_button.pack(side="left", padx=5)

# Task list frame (for incomplete tasks)
task_list_label = tk.Label(root, text="To Do", bg=color_pallete["rose_taupe"], fg=color_pallete["linen"],font=("Arial", 12, "bold"))
task_list_label.pack()
task_list_frame = tk.Frame(root, bg=color_pallete["old_rose"])
task_list_frame.pack(fill="x", pady=5, padx=10)

# Completed task list frame
task_completed_label = tk.Label(root, text="Completed Tasks",bg=color_pallete["rose_taupe"], fg=color_pallete["linen"],font=("Arial", 12, "bold"))
task_completed_label.pack()

completed_task_list_frame = tk.Frame(root, bg=color_pallete["rose_taupe"])
completed_task_list_frame.pack(fill="x", pady=5, padx=10)

# Initial render of tasks
update_task_list()

root.mainloop()
