# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox

# class TaskManagerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Task Manager")

#         # Sample data
#         self.employees = ["Alice", "Bob", "Charlie"]
#         self.tasks = ["Task 1", "Task 2", "Task 3"]

#         # Create and place widgets
#         self.create_widgets()

#     def create_widgets(self):
#         # Employee list
#         tk.Label(self.root, text="Select Employee:").pack(pady=5)
#         self.employee_combobox = ttk.Combobox(self.root, values=self.employees)
#         self.employee_combobox.pack(pady=5)

#         # Task list
#         tk.Label(self.root, text="Select Task:").pack(pady=5)
#         self.task_combobox = ttk.Combobox(self.root, values=self.tasks)
#         self.task_combobox.pack(pady=5)

#         # Assign button
#         self.assign_button = tk.Button(self.root, text="Assign Task", command=self.assign_task)
#         self.assign_button.pack(pady=20)

#     def assign_task(self):
#         employee = self.employee_combobox.get()
#         task = self.task_combobox.get()

#         if not employee or not task:
#             messagebox.showwarning("Input Error", "Please select both an employee and a task.")
#             return

#         # Here you would normally save the assignment to a database or file
#         # For this example, we'll just show a message
#         messagebox.showinfo("Task Assigned", f"Task '{task}' has been assigned to {employee}.")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = TaskManagerApp(root)
#     root.mainloop()


import tkinter as tk
from tkinter import ttk

def on_select(event):
    selected_value = combo.get()
    print(f"Selected value: {selected_value}")

root = tk.Tk()
root.title("Tkinter ComboBox Example")

# Create a combobox
combo = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combo.pack(padx=10, pady=10)

# Bind the selection event to the handler function
combo.bind("<<ComboboxSelected>>", on_select)

root.mainloop()
