from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox
import re

import database
import sidebar
from tkcalendar import Calendar
from datetime import datetime

# import sidebar2
import emphomemenu

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title("Emporium")
        self.root.geometry("900x600")
        self.root.resizable(False, False)
        
        self.login()  # Call the login method to display the login frame

        self.root.mainloop()

    def login(self):
        self.clear_frame()
        self.login_frame = Frame(self.root)
        self.login_frame.pack(fill=BOTH, expand=True)  # Make sure the frame is visible
        
        self.img = Image.open("Login.png")
        self.img_re = self.img.resize((900, 610))
        self.img_new = ImageTk.PhotoImage(self.img_re)
        self.img_label = Label(self.login_frame, image=self.img_new)
        self.img_label.place(x=-1, y=-1)
        self.img_label.image = self.img_new  # Keep a reference to avoid garbage collection

        self.name_entry = Entry(self.login_frame,width=28, border=0, bg='white', font=('Lexend Deca', 16, 'normal'))
        self.name_entry.place(x=493, y=249)

        self.pass_entry = Entry(self.login_frame,width=25, border=0, bg='white', font=('Lexend Deca', 16, 'normal'))
        self.pass_entry.place(x=493, y=346)

        self.btn = ctk.CTkButton(self.root,text="Login",hover_color= "#22282e",fg_color= "black",bg_color= "white",width=365 ,height= 41,font=('Lexend Deca', 22, 'bold'),command=self.getVallogin)
        self.btn.place(x=490, y=446)

        imglb = Image.open("regbtn.png")
        imglb_re = imglb.resize((280, 50))
        self.imglb_tk = ImageTk.PhotoImage(imglb_re)
        self.register_lb = Label(self.login_frame, image=self.imglb_tk, bg="red")
        self.register_lb.place(x=585, y=493, height=40, width=280)
        self.register_lb.bind("<Button-1>", lambda e: self.register())

        
    def getVallogin(self):
        uname = self.name_entry.get()
        pwd = self.pass_entry.get()
        patt = "[a-zA-Z0-9_.]+@[a-zA-Z]+.[a-zA-Z]{2,6}"
        data = (uname, pwd)
        if uname == "":
            messagebox.showwarning("warning", 'Username cannot be empty')
        elif pwd == "":
            messagebox.showwarning("warning", 'Password cannot be empty')
       
        
        elif uname == "Admin":
            res = database.loginAdminUsername(data)
            # res = database.employeeLogin(data)

            if res:
                messagebox.showinfo("Info", "Login Successfully")
                self.root.destroy()
                sidebar.HomeScreen()
            else:
                messagebox.showerror("Error", "User doesn't exist")
        
        elif uname == "admin@gmail.com":
            res = database.loginAdminEmail(data)
            if res:
                messagebox.showinfo("Info", "Login Successfully")
                self.root.destroy()
                sidebar.HomeScreen()
            else:
                messagebox.showerror("Error", "User doesn't exist")


        elif re.match(patt, uname):
            res = database.loginUserEmail(data)
            # res = database.employeeLogin(data)
            if res:
                messagebox.showinfo("Info", "Login Successfully")
                self.root.destroy()
                # sidebar.home_screen(res[0])
                # sidebar2.sidebar1(res[0])
                emphomemenu.createEmphomemenu(res[2],'login')

                print(res)
            else:
                messagebox.showerror("Error", "User doesn't exist")
        else:
            res = database.loginUserUsername(data)
            if res:
                messagebox.showinfo("Info", "Login Successfully")
                self.root.destroy()
                # sidebar.home_screen(res[0])
                # sidebar2.sidebar1(res[0])
                emphomemenu.createEmphomemenu(res[2],'login')
                print(res)
            else:
                messagebox.showerror("Error", "User doesn't exist")

    

    def register(self):
        self.clear_frame()
        self.register_frame = Frame(self.root)
        self.register_frame.pack(fill= BOTH,expand=True) 
        self.img = Image.open("Register.png")
        self.img_re = self.img.resize((900, 610))
        self.img_new = ImageTk.PhotoImage(self.img_re)
        self.img_label = Label(self.register_frame, image=self.img_new)
        self.img_label.place(x=-1, y=-1)
        self.img_label.image = self.img_new 


        self.name_entry = Entry(self.register_frame,width=28, border=0, bg='white', font=('Lexend Deca', 16, 'normal'))
        self.name_entry.place(x=476, y=165)

        self.email_entry = Entry(self.register_frame,width=28, border=0, bg='white', font=('Lexend Deca', 16, 'normal'))
        self.email_entry.place(x=476, y=242)
        
        self.dob_entry = Entry(self.register_frame,width=28, border=0, bg='white', font=('Lexend Deca', 16, 'normal'))
        self.dob_entry.place(x=476, y=319)
        self.dob_entry.insert(0, "yyyy/dd/mm")
        self.dob_entry.bind("<1>", self.pick_date)

        self.dept_entry = Entry(self.register_frame,width=28, border=0, bg='white', font=('Lexend Deca', 16, 'normal'))
        self.dept_entry.place(x=476, y=391)

        self.but = ctk.CTkButton(self.register_frame,text="Register",hover_color= "#22282e",fg_color= "black",bg_color= "white",width=396 ,height= 42,font=('Lexend Deca', 16, 'bold'),command=self.getValregister)
        self.but.place(x=473, y=458)

        imglb = Image.open("btt.png")
        imglb_re = imglb.resize((280, 50))
        self.imglb_tk = ImageTk.PhotoImage(imglb_re)
        self.login_lb = Label(self.register_frame, image=self.imglb_tk, bg="white")
        self.login_lb.place(x=600, y=500, height=30, width=280)
        self.login_lb.bind("<Button-1>",lambda e: self.login())

    def pick_date(self, event):
           date_window = Toplevel(self.register_frame)
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

    def getValregister(self):
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

   

    def clear_frame(self):
        # Clear any existing frames
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    Main()
