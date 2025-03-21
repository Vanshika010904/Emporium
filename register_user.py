from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime
from PIL import Image, ImageTk
import re
import database
import login

class regUserScreen:
    def __init__(self):
        self.root = Tk()
        self.root.title("Register")
        self.root.geometry("900x600")

        self.root.resizable(False, False)
        img = Image.open("register.png")
        img_re = img.resize((900, 600))
        self.img_tk = ImageTk.PhotoImage(img_re)
        img_label = Label(self.root, image=self.img_tk)
        img_label.place(x=-1, y=-1)

        self.name_entry = Entry(self.root, width=23, border=0, bg='white', font=('Lexend Deca', 18, 'normal'))
        self.name_entry.place(x=480, y=174)

        self.email_entry = Entry(self.root, width=23, border=0, bg='white', font=('Lexend Deca', 18, 'normal'))
        self.email_entry.place(x=480, y=250)

        self.dob_entry = Entry(self.root, width=20, border=0, bg='white', font=('Lexend Deca', 18, 'normal'))
        self.dob_entry.place(x=480, y=325)
        self.dob_entry.insert(0, "yyyy/dd/mm")
        self.dob_entry.bind("<1>", self.pick_date)

        self.dept_entry = Entry(self.root, width=23, border=0, bg='white', font=('Lexend Deca', 18, 'normal'))
        self.dept_entry.place(x=480, y=403)

        self.btn = Button(self.root, text="Register", bg="black", fg="white", font=('Lexend Deca', 16, 'bold'), border=0, height=0, width=28, command=self.getVal)
        self.btn.place(x=480, y=473)

        imga = Image.open("btt.png")
        img_ree = imga.resize((280, 50))
        self.img_tkk = ImageTk.PhotoImage(img_ree)
        self.login_lb = Label(self.root, image=self.img_tkk, bg="red")
        self.login_lb.place(x=600, y=520, height=40, width=280)

        self.login_lb.bind("<Button-1>", self.open_login_screen)

        self.root.mainloop()

    def pick_date(self, event):
        date_window = Toplevel(self.root)
        date_window.grab_set()
        date_window.title('Choose a Date of birth')
        date_window.geometry('250x220+590+370')

        self.cal = Calendar(date_window, selectmode='day', date_pattern="yyyy-mm-dd")
        self.cal.place(x=0, y=0)

        submit_btn = Button(date_window, text="Submit", command=self.grab_date)
        submit_btn.place(x=80, y=190)

    def grab_date(self):
        self.dob_entry.delete(0, END)
        self.dob_entry.insert(0, self.cal.get_date())
        self.cal.master.destroy()

    def getVal(self):
        uname = self.name_entry.get()
        dob = self.dob_entry.get()
        email = self.email_entry.get()
        dept = self.dept_entry.get()

        patt = "[a-zA-Z0-9_.]+@[a-zA-Z]+.[a-zA-Z]{2,6}"
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print("Formatted Date and Time:", formatted_datetime)
        data = (uname, email, dept, dob, formatted_datetime)
        if uname == "":
            messagebox.showwarning("warning", 'Username cannot be empty')
        elif email == "":
            messagebox.showwarning("warning", 'Email cannot be empty')
        elif dept == "":
            messagebox.showwarning("warning", 'Department cannot be empty')
        elif re.match(patt, email) is None:
            messagebox.showwarning("Warning", "Invalid Email")
        else:
            res = database.registerUser(data)
            if res:
                messagebox.showinfo("Info", "Successfully registered ")
                
            else:
                messagebox.showinfo("Warning", "Not registered")

    def open_login_screen(self, event):
        self.root.destroy()
        login.loginScreen()

if __name__ == "__main__":
    regUserScreen()
