import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import database

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        # self.root.title("Task Management")

        # Create and place widgets
        tk.Label(self.root, text="Task Title:").grid(row=0, column=0, padx=10, pady=10)
        self.title_entry = tk.Entry(self.root)
        self.title_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Description:").grid(row=1, column=0, padx=10, pady=10)
        self.description_entry = tk.Text(self.root, height=4, width=30)
        self.description_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Due Date (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=10)
        self.due_date_entry = tk.Entry(self.root)
        self.due_date_entry.grid(row=2, column=1, padx=10, pady=10)

        self.employees = ["Alice", "Bob", "Charlie"]
        self.tasks = ["Task 1", "Task 2", "Task 3"]

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Employee list
        tk.Label(self.root, text="Select Employee:").grid(row=4, column=0, padx=10, pady=10)
        self.employee_combobox = ttk.Combobox(self.root, values=self.employees)
        self.employee_combobox.grid(row=4, column=1, padx=10, pady=10)

        tk.Button(self.root, text="Add Task", command=self.add_task).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Clear", command=self.clear_form).grid(row=6, column=0, columnspan=2, pady=10)

    def add_task(self):
        """Add a task to the in-memory storage (or to the database)."""
        title = self.title_entry.get()
        description = self.description_entry.get("1.0", tk.END).strip()
        due_date = self.due_date_entry.get()
        name= self.employee_combobox.get()
        print(f"Selected value: {name}")

        if not title or not due_date:
            messagebox.showwarning("Input Error", "Title and Due Date are required.")
            return

        # Print task information to console (for debugging purposes)
        print(f"Task Title: {title}")
        print(f"Description: {description}")
        print(f"Due Date: {due_date}")
        print(f"Name: {name}")

        # Add task to the database
        data = (title, description, due_date,name)
        res = database.task(data)
        
        if res:
            messagebox.showinfo("Success", "Task has been added successfully!")
        else:
            messagebox.showerror("Error", "Task could not be added.")

        # Clear the form after adding the task
        self.clear_form()

    def clear_form(self):
        """Clear the form entries."""
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete("1.0", tk.END)
        self.due_date_entry.delete(0, tk.END)
        self.employee_combobox.set('')

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()


# import tkinter as tk
# import tkinter as ttk
# from tkinter import messagebox
# import database
# class td:
#     def __init__(self, root):
#         self.root = root
#         # self.root.title("Task Management")

#         # Create and place widgets
#         tk.Label(self.root, text="Task Title:").grid(row=0, column=0, padx=10, pady=10)
#         self.title_entry = tk.Entry(self.root)
#         self.title_entry.grid(row=0, column=1, padx=10, pady=10)

#         tk.Label(self.root, text="Description:").grid(row=1, column=0, padx=10, pady=10)
#         self.description_entry = tk.Text(self.root, height=4, width=30)
#         self.description_entry.grid(row=1, column=1, padx=10, pady=10)

#         tk.Label(self.root, text="Due Date (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=10)
#         self.due_date_entry = tk.Entry(self.root)
#         self.due_date_entry.grid(row=2, column=1, padx=10, pady=10)

#         self.employees = ["Alice", "Bob", "Charlie"]
#         self.tasks = ["Task 1", "Task 2", "Task 3"]

#         # Create and place widgets
#         self.create_widgets()

#     def create_widgets(self):
#         # Employee list
#         tk.Label(self.root, text="Select Employee:").pack(pady=5)
#         self.employee_combobox = ttk.Combobox(self.root, values=self.employees)
#         self.employee_combobox.pack(pady=5)

#         tk.Button(self.root, text="Add Task", command=self.add_task).grid(row=3, column=0, columnspan=2, pady=10)
#         tk.Button(self.root, text="Clear", command=self.clear_form).grid(row=4, column=0, columnspan=2, pady=10)

#     def add_task(self):
#         """Add a task to the in-memory storage (or print to console)."""
#         title = self.title_entry.get()
#         description = self.description_entry.get("1.0", tk.END).strip()
#         due_date = self.due_date_entry.get()

#         if not title or not due_date:
#             messagebox.showwarning("Input Error", "Title and Due Date are required.")
#             return
#         print(f"Task Title: {title}")
#         print(f"Description: {description}")
#         print(f"Due Date: {due_date}")
#         messagebox.showinfo("Success", "Task added successfully!")
#         data=(title,description,due_date)
#         res = database.task(data)
#         if res:
#                     messagebox.showinfo("Info","task has been added Sucessfully")
#                     # res = database.deletePendingUser(rowId)
#                     # self.refresh_table()
#         else:
#                     messagebox.showinfo("Info","task not added")
#         # Simulate adding the task (print to console or store in a list)
#         self.clear_form()

#     def clear_form(self):
#         """Clear the form entries."""
#         self.title_entry.delete(0, tk.END)
#         self.description_entry.delete("1.0", tk.END)
#         self.due_date_entry.delete(0, tk.END)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = td(root)
#     root.mainloop()
