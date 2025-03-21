from cgitb import text
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import ttk

from PIL import Image, ImageTk
import viewaddtask
import viewassigntask
import database


class createAddTask:

    # constructor
    def __init__(self, window):
        self.root = window

    def firstFrame(self):

        # create a frame
        self.mainFrame = Frame(self.root)
        self.mainFrame.place(x = 0, y = 0, width="800", height="600")

        self.my_label=Label(self.root,text="Assign Tasks",font=("Mongolian Baiti",20))
        self.my_label.place(x=50,y=30,width="200")


        # set background image
        self.image = Image.open('menuimage1.jpg')
        self.img=self.image.resize((450,600))
        self.newimage=ImageTk.PhotoImage(self.img)
        self.bgLabel = Label(self.mainFrame, image=self.newimage)
        self.bgLabel.place(x = 350, y =  0,  width="450", height = "600")

        self.EmpIdLabel = Label(self.mainFrame, text="Emp Id",font=("Mongolian Baiti",16))
        self.EmpIdLabel.place(x = 15, y = 100, width="120")

        self.emp = database.nameEmp()
        self.empName = StringVar()
        self.EmpIdEntry = ttk.Combobox(self.mainFrame,value=self.emp, textvariable=self.empName)
        self.EmpIdEntry.place(x = 150, y = 100, width="150",height=30)        
        # self.EmpIdEntry = Entry(self.mainFrame)
        # self.EmpIdEntry.place(x = 150, y = 100, width="150",height=30)
        self.Taskname = Label(self.mainFrame, text="Task Name",font=("Mongolian Baiti",16))
        self.Taskname.place(x = 30, y = 150, width="120")

        self.Task = database.nameTask()
        self.TaskName = StringVar()
        self.TasknameEntry = ttk.Combobox(self.mainFrame,value=self.Task, textvariable=self.TaskName)
        self.TasknameEntry.place(x = 150, y = 150, width="150",height=30)

        self.StartdateLabel = Label(self.mainFrame, text="Start Date",font=("Mongolian Baiti",16))
        self.StartdateLabel.place(x = 25, y = 200, width="120")

        self.startData = StringVar()
        self.StartdateEntry = DateEntry(self.mainFrame, textVariable = self.startData,date_pattern='yyyy-MM-dd')
        self.StartdateEntry.place(x = 150, y = 200, width="150",height=30)

        self.EnddateLabel = Label(self.mainFrame, text="End Date",font=("Mongolian Baiti",16))
        self.EnddateLabel.place(x = 25, y = 250, width="120")

        self.endData = StringVar()
        self.EnddateEntry = DateEntry(self.mainFrame, textVariable = self.endData,date_pattern='yyyy-MM-dd')
        self.EnddateEntry.place(x = 150, y = 250, width="150",height=30)
       

        self.submit = Button(self.mainFrame, text = "Submit", command=self.create,font=("Mongolian Baiti",16),bg="white")
        self.submit.place(x = 50, y = 320, width="70")
        
        self.root.mainloop()

    def create(self):
        self.data = [
            self.empName.get(), 
            self.TasknameEntry.get(),  
            self.StartdateEntry.get(),
            self.EnddateEntry.get(),
            'pending'
        ]
        print(self.data)
        if (self.empName.get() == ''):
            messagebox.showinfo('Alert', 'Enter your EmpId.')
        elif self.TasknameEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Task Name.')
        elif self.StartdateEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Start Date.')
        elif self.EnddateEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your End Date.')
        else:
            res = database.assigntask(self.data)
            if res:
                messagebox.showinfo('Alert','Submitted Successfully')
                self.empName.delete(0,END)
                self.TasknameEntry.delete(0,END)
                self.StartdateEntry.delete(0,END)
                self.EnddateEntry.delete(0,END)
                # obj = viewassigntask.viewAssignTask(self.root)
                # obj.manageTask()
            else:
                messagebox.showinfo('Alert', 'Something went wrong.')







if __name__ == '__main__':
    obj = createAddTask()
    obj.firstFrame()