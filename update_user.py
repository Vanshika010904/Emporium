from tkinter import *
from tkinter import messagebox
import database
import view_user

class Home:
    def __init__(self, id, parent_view):
        self.root = Tk()
        self.root.geometry('600x400')
        self.root.title("Update User")
        self.id = id
        self.parent_view = parent_view
        
        self.data = database.getSingleUser(self.id)
        print("Data is --------- ", self.data)
        
        self.frame1 = Frame(self.root, bg='#8fb3bd', height=300, width=400)
        self.frame1.place(x=100, y=50)
 
        self.name = Label(self.frame1, text="Name", font=('Consolas', 15, 'normal'), bg="#8fb3bd")
        self.name.place(x=40, y=80)
        
        self.name_entry = Entry(self.frame1, font=('Consolas', 15, 'normal'))
        self.name_entry.place(x=140, y=80)
        self.name_entry.insert(0, self.data[1])    
        
        self.mail = Label(self.frame1, text="Email", font=('Consolas', 15, 'normal'), bg="#8fb3bd")
        self.mail.place(x=40, y=130)
        
        self.mail_entry = Entry(self.frame1, font=('Consolas', 15, 'normal'))
        self.mail_entry.place(x=140, y=130)
        self.mail_entry.insert(0, self.data[2])    
        
        self.pwd = Label(self.frame1, text="Password", font=('Consolas', 15, 'normal'), bg="#8fb3bd")
        self.pwd.place(x=40, y=180)
        
        self.pass_entry = Entry(self.frame1, font=('Consolas', 15, 'normal'))
        self.pass_entry.place(x=140, y=180)
        self.pass_entry.insert(0, self.data[3])    
        
        self.btn = Button(self.frame1, text="Update", font=('Consolas', 15, 'normal'), command=self.getVal)
        self.btn.place(x=150, y=230)
            
        self.root.mainloop()

    def getVal(self):
        data = (self.name_entry.get(), self.mail_entry.get(), self.pass_entry.get(), self.id[0])
        
        res = database.updateUser(data)
        if res:
            result = messagebox.showinfo("Updated", "User Update Successfully")
            if result:
                self.root.destroy()
                self.parent_view.refresh_table()
        else:
            messagebox.showerror("Update", "Not Updated")
        
if __name__ == "__main__":
    # This block is for testing purposes; in actual use, it should be called with appropriate arguments
    obj = Home(1, None)
