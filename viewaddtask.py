from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import database
import edittask

class viewAddTask():
    # constructor
    def __init__(self, window):
        self.root = window

    def manageTask(self):
        self.fr = Frame(self.root, bg="Grey")
        self.fr.place(x=0, y=0, width="800", height="500")

        self.tr = Treeview(self.fr, columns=('A', 'B', 'C', 'E', 'F', 'G','H', 'I'), selectmode="extended")

        self.tr.heading('#0', text="Id")
        self.tr.column('#0', minwidth=0, width=60, stretch=NO)

        self.tr.heading('#1', text="Project Name")
        self.tr.column('#1', minwidth=0, width=130, stretch=NO)

        self.tr.heading('#2', text="Task Name")
        self.tr.column('#2', minwidth=0, width=80, stretch=NO)
        
        self.tr.heading('#3', text="Edit")
        self.tr.column('#3', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#4', text="Delete")
        self.tr.column('#4', minwidth=0, width=80, stretch=NO)

        data = database.allTask()
        # print(data)
        for i in data:
            self.tr.insert('', 0, text = i[0], values=(i[1], i[2], 'Edit', 'Delete'))
        
 
      
        # create double action button
        self.tr.bind('<Double-Button-1>', self.actions)
        self.tr.place(x=0, y=0,height=500,width=800)
        self.root.mainloop()
    


    def actions(self, e):
        # get the values of the selected rows\\
        tt = self.tr.focus()

        # get the column id
        col = self.tr.identify_column(e.x)
        # print(col)
        # print(self.tr.item(tt))

        gup = (
            self.tr.item(tt).get('text'),
        )
        
       
        if col == '#4':
            response = messagebox.askyesno('Delete','Do you really want to delete?')
            if response:
                print("Checking the data which is being passed to delete task this print statement is present in ViewAddTask line 64",gup)
                a = database.deleteTask(gup[0])
                if a:
                    messagebox.showinfo('Success', 'task deleted successfully.')
                    obj = viewAddTask(self.root)
                    obj.manageTask()
                else:
                    messagebox.showinfo('Alert', 'Something went wrong.')

        if col =="#3":
            obj = edittask.createEditTask(self.root)
            obj.firstFrame(gup)




if __name__ == '__main__':
    obj = viewAddTask()
    obj.manageTask()
        

# from tkinter import *
# from tkinter.ttk import Treeview
# from tkinter import messagebox
# import database
# import edittask

# class ViewAddTask:
#     def __init__(self, window):
#         self.root = window
#         self.manageTask()

#     def manageTask(self):
#         self.fr = Frame(self.root, bg="Grey")
#         self.fr.place(x=0, y=0, width=800, height=500)

#         self.tr = Treeview(self.fr, columns=('A', 'B', 'C', 'E', 'F', 'G', 'H', 'I'), selectmode="extended")

#         self.tr.heading('#0', text="Id")
#         self.tr.column('#0', minwidth=0, width=60, stretch=NO)

#         self.tr.heading('#1', text="Project Name")
#         self.tr.column('#1', minwidth=0, width=130, stretch=NO)

#         self.tr.heading('#2', text="Task Name")
#         self.tr.column('#2', minwidth=0, width=80, stretch=NO)

#         self.tr.heading('#3', text="Edit")
#         self.tr.column('#3', minwidth=0, width=80, stretch=NO)

#         self.tr.heading('#4', text="Delete")
#         self.tr.column('#4', minwidth=0, width=80, stretch=NO)

#         self.loadData()

#         # Create double action button
#         self.tr.bind('<Double-1>', self.actions)
#         self.tr.place(x=0, y=0, height=500, width=800)

#     def loadData(self):
#         try:
#             data = database.allTask()
            
#             # Check if data is a list
#             if not isinstance(data, list):
#                 raise ValueError("Data from database.allTask() is not a list.")
            
#             self.tr.delete(*self.tr.get_children())  # Clear existing data
            
#             # Check that each item in data is a tuple with at least 3 elements
#             for i in data:
#                 if not isinstance(i, (tuple, list)) or len(i) < 3:
#                     raise ValueError("Data item is not a tuple or list with at least 3 elements.")
                
#                 self.tr.insert('', 'end', text=i[0], values=(i[1], i[2], 'Edit', 'Delete'))
        
#         except Exception as e:
#             print(f"Error loading data: {e}")
#             messagebox.showerror("Error", f"Failed to load data: {e}")

#     def actions(self, e):
#         try:
#             item = self.tr.selection()[0]
#             column_id = self.tr.identify_column(e.x)
#             if not column_id:
#                 raise ValueError("Could not identify the column.")

#             if column_id == '#4':
#                 response = messagebox.askyesno('Delete', 'Do you really want to delete?')
#                 if response:
#                     item_id = self.tr.item(item, 'text')
#                     success = database.deleteTask(item_id)
#                     if success:
#                         messagebox.showinfo('Success', 'Task deleted successfully.')
#                         self.loadData()  # Reload data after deletion
#                     else:
#                         messagebox.showinfo('Alert', 'Something went wrong.')

#             if column_id == '#3':
#                 item_id = self.tr.item(item, 'text')
#                 edit_window = edittask.createEditTask(self.root)
#                 edit_window.firstFrame(item_id)
#         except Exception as e:
#             print(f"Error in actions: {e}")
#             messagebox.showerror("Error", f"An error occurred: {e}")

# if __name__ == '__main__':
#     root = Tk()
#     root.geometry("800x500")
#     app = ViewAddTask(root)
#     root.mainloop()
