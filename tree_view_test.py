import tkinter as tk
from tkinter import ttk

class Task:
    def __init__(self, task_id, description, parent):
        self.task_id = task_id
        self.description = description
        self.parent = parent

class TreeViewer:
    def __init__(self, root):
        self.root = root
        self.root.title=("Treviewer Test Window")
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=5)
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        # Task List (Treeview)
        self.tree = ttk.Treeview(root, columns=("Task", "Completed"), show="headings", height=10)
        self.tree.heading("Task", text="Task")
        self.tree.heading("Completed", text="Completed")
        self.tree.column("Task", width=300)
        self.tree.column("Completed", width=100)
        self.tree.pack(pady=5)

    def add_task(self):
        task_description = self.task_entry.get()
        task = Task(self, self.task_id, task_description)
        self.tasks[self.task_id] = task  # Store Task object

        self.tree.insert("","end", iid=self.task_id, values=(self.task_entry, "test"))
        


if __name__ == "__main__":
    root = tk.Tk()
    app = TreeViewer(root)
    root.mainloop()