from tkinter import *
from tkinter import messagebox
import re
from PIL import Image, ImageTk
import register_user
import database
import sidebar

class loginScreen:
    def __init__(self):
        self.root = Tk()
        self.root.title("Login")
        self.root.geometry("900x600")

        self.root.resizable(False, False)
        img = Image.open("emporiumFinal.png")
        img_re = img.resize((900, 610))
        self.img_new = ImageTk.PhotoImage(img_re)
        img_label = Label(self.root, image=self.img_new)
        img_label.place(x=-1, y=-1)

        self.name_entry = Entry(self.root, width=23, border=0, bg='white', font=('Lexend Deca', 18, 'normal'))
        self.name_entry.place(x=493, y=253)

        self.pass_entry = Entry(self.root, width=20, border=0, bg='white', font=('Lexend Deca', 18, 'normal'))
        self.pass_entry.place(x=493, y=350)

        self.btn = Button(self.root, text="Login", bg="black", fg="white", font=('Kanit', 15, 'bold'), border=0, height=1, width=29, command=self.getVal)
        self.btn.place(x=493, y=450)

        imglb = Image.open("regbtn.png")
        imglb_re = imglb.resize((280, 50))
        self.imglb_tk = ImageTk.PhotoImage(imglb_re)
        self.register_lb = Label(self.root, image=self.imglb_tk, bg="red")
        self.register_lb.place(x=585, y=493, height=35, width=280)
        self.register_lb.bind("<Button-1>", self.open_register_screen)

        self.root.mainloop()

    def getVal(self):
        uname = self.name_entry.get()
        pwd = self.pass_entry.get()
        patt = "[a-zA-Z0-9_.]+@[a-zA-Z]+.[a-zA-Z]{2,6}"
        data = (uname, pwd)
        if uname == "":
            messagebox.showwarning("warning", 'Username cannot be empty')
        elif pwd == "":
            messagebox.showwarning("warning", 'Password cannot be empty')
        elif len(pwd) < 8:
            messagebox.showwarning("warning", 'Password must contain at least 8 characters')
        
        elif uname == "Admin":
            res = database.loginAdminUsername(data)
            if res:
                messagebox.showinfo("Info", "Login Successfully")
                self.root.destroy()
                sidebar.home_screen()
                print(res)
            else:
                messagebox.showerror("Error", "User doesn't exist")
        
        elif uname == "admin@gmail.com":
            res = database.loginAdminEmail(data)
            if res:
                messagebox.showinfo("Info", "Login Successfully")
                self.root.destroy()
                sidebar.home_screen()
                print(res)
            else:
                messagebox.showerror("Error", "User doesn't exist")


        elif re.match(patt, uname):
            res = database.loginUserEmail(data)
            print("res after ------", res)
            if res:
                messagebox.showinfo("Info", "Login Successfully")
                self.root.destroy()
                sidebar.home_screen()
                print(res)
            else:
                messagebox.showerror("Error", "User doesn't exist")
        else:
            res = database.loginUserUsername(data)
            if res:
                messagebox.showinfo("Info", "Login Successfully")
                self.root.destroy()
                sidebar.home_screen()
                print(res)
            else:
                messagebox.showerror("Error", "User doesn't exist")

    def open_register_screen(self, event):
        self.root.destroy()
        register_user.regUserScreen()

if __name__ == "__main__":
    loginScreen()
