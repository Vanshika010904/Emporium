
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import database
import update_user

class showUsers:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.create_table()

    def create_table(self):
        self.table = ttk.Treeview(self.parent_frame, columns=["id", 'Name', 'Email', 'Password', 'Edit', 'Delete'], show='headings')

        self.table.heading('#1', text="Id")
        self.table.heading('#2', text="Name")
        self.table.heading('#3', text="Email")
        self.table.heading('#4', text="Password")
        self.table.heading('#5', text="Edit")
        self.table.heading('#6', text="Delete")

        self.table.column("#1", width=80)
        self.table.column("#2", width=100)
        self.table.column("#3", width=140)
        self.table.column("#4", width=100)
        self.table.column("#5", width=70)
        self.table.column("#6", width=70)

        self.populate_table()

        style = ttk.Style()
        style.theme_use('default')
        self.table.bind('<Double-Button-1>', self.actions)

        self.table.pack(fill=BOTH, expand=True)

    def populate_table(self):
        for row in self.table.get_children():
            self.table.delete(row)

        res = database.allUsers()


        for i in res:
            
            self.table.insert('', 'end', text=i[0], values=(i[0], i[1], i[2], i[3], 'Edit', 'Delete'))

    def actions(self, event):
        tc = self.table.focus()
        col = self.table.identify_column(event.x)
        
        rowId = (self.table.item(tc).get('text'),)
        print("column is ", col)
        print("rowId is ", rowId)

        if col == "#6":
            res = messagebox.askyesno("Delete", "Do you really want to delete this item?")
            if res:
                result = database.deleteUser(rowId)
                if result:
                    messagebox.showinfo("Deleted", "User Deleted Successfully")
                    self.refresh_table()

        if col == "#5":
            res = messagebox.askyesno("Edit", "Do you really want to Edit this item?")
            if res:
                update_user.Home(rowId, self)

    def refresh_table(self):
        for widget in self.parent_frame.winfo_children():
            widget.destroy()
        self.create_table()
