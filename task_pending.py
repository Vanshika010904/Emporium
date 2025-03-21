import tkinter as tk
from tkinter import ttk

class Task:
    def __init__(self, root):
        self.root = root
        # self.root.title("Task Management Table")

        # Create the Treeview widget
        self.columns = ("sr_no", "task_assigned", "pending", "deadline")
        self.tree = ttk.Treeview(self.root, columns=self.columns, show='headings')

        # Define the column headings
        self.tree.heading("sr_no", text="Sr. No.")
        self.tree.heading("task_assigned", text="Task Assigned")
        self.tree.heading("pending", text="Pending")
        self.tree.heading("deadline", text="Deadline")

        # Define the column widths
        self.tree.column("sr_no", width=50, anchor=tk.CENTER)
        self.tree.column("task_assigned", width=150, anchor=tk.W)
        self.tree.column("pending", width=100, anchor=tk.CENTER)
        self.tree.column("deadline", width=100, anchor=tk.CENTER)

        # Pack the Treeview widget into the window
        self.tree.pack(expand=True, fill=tk.BOTH)

        # Populate the Treeview with data
        self.populate_treeview()

    def populate_treeview(self):
        # Sample data
        data = [
            (1, "Task 1", "Yes", "2024-08-01"),
            (2, "Task 2", "No", "2024-08-05"),
            (3, "Task 3", "Yes", "2024-08-10"),
        ]
        
        # Insert data into the Treeview
        for item in data:
            self.tree.insert("", tk.END, values=item)

def main():
    # Create the main application window
    root = tk.Tk()
    
    # Create an instance of the Task class
    task_app = Task(root)
    
    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()
