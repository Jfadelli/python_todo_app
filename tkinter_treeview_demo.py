import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Treeview Example")

# Create Treeview widget
tree = ttk.Treeview(root, columns=("Name", "Age", "City"))
tree.heading("#0", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("City", text="City")

# Insert data into Treeview
tree.insert("", tk.END, text="1", values=("John", 25, "New York"))
tree.insert("", tk.END, text="2", values=("Mary", 30, "Los Angeles"))
tree.insert("1", tk.END, text="3", values=("Bob", 20, "Chicago"))  # Child of John

# Pack the Treeview widget
tree.pack()

# Run the main loop
root.mainloop()