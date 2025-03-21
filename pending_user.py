from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import database
import update_user
from datetime import datetime
import num
import io
from PIL import Image, ImageTk

class pendingUserList:
    def __init__(self,parent_frame):
        self.parent_frame = parent_frame
        self.create_table()

    def create_table(self):
        self.table = ttk.Treeview(self.parent_frame, columns=["id", 'Name', 'Email', 'Dept','Dob', 'Confirm', 'Delete'], show='headings')

        self.table.heading('#1', text="Id")
        self.table.heading('#2', text="Name")
        self.table.heading('#3', text="Email")
        self.table.heading('#4', text="Department")
        self.table.heading('#5', text="DOB")
        self.table.heading('#6', text="Confirm")
        self.table.heading('#7', text="Delete")

        self.table.column("#1", width=80)
        self.table.column("#2", width=100)
        self.table.column("#3", width=140)
        self.table.column("#4", width=100)
        self.table.column("#5", width=100)
        self.table.column("#6", width=70)
        self.table.column("#7", width=70)

        self.populate_table()

        style = ttk.Style()
        style.theme_use('default')
        self.table.bind('<Double-Button-1>', self.actions)

        self.table.pack(fill=BOTH, expand=True)

    def populate_table(self):
        for row in self.table.get_children():
            self.table.delete(row)

        res = database.allPendingUsers()

        for i in res:
            print(i)
            self.table.insert('','end',text= i[0],values=(i[0],i[1],i[2],i[3],i[4],'Confirm','Delete'))

    def actions(self, event):
        tc = self.table.focus()
        col = self.table.identify_column(event.x)
        
        rowId = (self.table.item(tc).get('text'),)
        print("column is ", col)
        print("rowId is ", rowId)
        




        if col == "#7":
            res = messagebox.askyesno("Delete", "Do you really want to delete this item?")
            if res:
                result = database.deletePendingUser(rowId)
                if result:
                    messagebox.showinfo("Deleted", "User Deleted Successfully")
                    self.refresh_table()

        if col == "#6":
            res = messagebox.askyesno("Edit", "Do you really want to confirm this request?")
            if res:

                temp = database.getSinglePendingUser(rowId)
                print(temp)
               
                name = temp[1].strip()  # Remove any leading or trailing whitespace
                date = temp[4]
                use=name.lower()
                s=num.read_and_increment_number()
                username=f"{use}{s}"
               
                formatted_string = f"{name}{date.year}{date.month}{date.day}"
                # print(formatted_string)
                binary_data=self.convert_to_binary_data("im.png")
                
                data = (temp[1],temp[2],formatted_string,temp[4],temp[3],binary_data,temp[5],username)
                print(data)
                res = database.addEmployee(data)
                if res:
                    messagebox.showinfo("Info","User has been added Sucessfully")
                    res = database.deletePendingUser(rowId)
                    self.refresh_table()
                else:
                    messagebox.showinfo("Info","User not added")


    def refresh_table(self):
        for widget in self.parent_frame.winfo_children():
            widget.destroy()
        self.create_table()
    
    def convert_to_binary_data(self, filename):
        with open(filename, 'rb') as file:
            binary_data = file.read()
        return binary_data
    


    # data = passed_data
    # print(data)
    # self.user_data = database.getSingleUser((data,))
        
    # image = Image.open(io.BytesIO(self.user_data[6]))
    # image = image.resize((200, 200), Image.LANCZOS)
    # self.image = ImageTk.PhotoImage(image)
    
    
    # with open('numbers.txt', 'w') as f:
    #     for i in range(1, 10001):
    #         f.write(f"{i}\n")
    # # with open('current.txt', 'r') as f:
    # #     for i in range(1, 10001):
    # #         f.write(f"{i}\n")