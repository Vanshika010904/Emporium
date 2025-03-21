from cgitb import text
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import ttk
from PIL import Image, ImageTk
import viewaddtask
import database


class createAddTask:

    # constructor
    def __init__(self, window):
        self.root = window
        

    def firstFrame(self):

        # create a frame
        self.mainFrame = Frame(self.root)
        self.mainFrame.place(x = 0, y = 0, width="800", height="600")

        self.my_label=Label(self.root,text="Add Task",font=("Mongolian Baiti",20))
        self.my_label.place(x=50,y=30,width="200")


        # set background image
        self.image = Image.open('menuimage1.jpg')
        self.img=self.image.resize((450,600))
        self.newimage=ImageTk.PhotoImage(self.img)
        self.bgLabel = Label(self.mainFrame, image=self.newimage)
        self.bgLabel.place(x = 350, y =  0,  width="450", height = "600")
      
        # self.EmpIdEntry = Entry(self.mainFrame)
        # self.EmpIdEntry.place(x = 150, y = 100, width="150",height=30)
        self.projectLabel = Label(self.mainFrame, text="Project",font=("Mongolian Baiti",16))
        self.projectLabel.place(x = 15, y = 100, width="120")

        self.project = database.namePro()
        print(self.project)
        # self.project = ['a', 'b', 'c']
        self.projectName = StringVar()
        self.projectEntry = ttk.Combobox(self.mainFrame,value=self.project, textvariable=self.projectName)
        self.projectEntry.place(x = 150, y = 100, width="150",height=30)


        self.Taskname = Label(self.mainFrame, text="Task Name",font=("Mongolian Baiti",16))
        self.Taskname.place(x = 30, y = 160, width="120")

        self.TasknameEntry = Entry(self.mainFrame)
        self.TasknameEntry.place(x = 150, y = 160, width="150",height=30)
       

        self.submit = Button(self.mainFrame, text = "Submit", command=self.create,font=("Mongolian Baiti",16),bg="white")
        self.submit.place(x = 150, y = 240, width="70")
        
        # self.backBtn=Button(self.mainFrame,text="Back",font=("Mongolian Baiti",16),bg="white", command= self.back)
        # self.backBtn.place(x=230,y=240,width="70",height=40)
        
        self.root.mainloop()

    def create(self):

        # print(tuple(self.projectName.get()))
        # print(self.projectName.get()[0])
        self.data = [
            self.projectEntry.get(),
            self.TasknameEntry.get()
        ]

        if self.projectEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Project.')
        elif self.TasknameEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Tasks.')
        else:
            res = database.addtask(self.data)
            if res:
                messagebox.showinfo('Alert','Submitted Successfully')
                # obj = viewaddtask.viewAddTask(self.root)
                # obj.manageTask()
                self.projectEntry.delete(0,END)
                self.TasknameEntry.delete(0,END)
            else:
                messagebox.showinfo('Alert', 'Something went wrong.')





if __name__ == '__main__':
    obj = createAddTask()
    obj.firstFrame()