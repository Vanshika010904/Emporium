from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry

from PIL import Image, ImageTk
import viewaddproject

import database

class createEditProject:

    # constructor
    def __init__(self, window):
        self.root = window


    def firstFrame(self,gup):
        self.Id = gup[0] 
        # create a frame
        self.mainFrame = Frame(self.root,bg="white")
        self.mainFrame.place(x = 0, y = 0, width="800", height="500")

        self.my_label=Label(self.mainFrame,text="EDIT PROJECT",font=("Mongolian Baiti",20),bg="white")
        self.my_label.place(x=50,y=30,width="270")
                        
    
        # set background image
        
        self.image = ImageTk.PhotoImage(Image.open('editemp.jpg'))
        self.bgLabel = Label(self.mainFrame, image=self.image)
        self.bgLabel.place(x = 350, y =  0,  width="800", height = "500")


        self.NameLabel = Label(self.mainFrame, text="Project Name",font=("Mongolian Baiti",16),bg="white")
        self.NameLabel.place(x = 30, y = 100, width="120")

        self.NameEntry = Entry(self.mainFrame)
        self.NameEntry.place(x = 150, y = 100, width="150",height=30)

        self.DetailsLabel = Label(self.mainFrame, text="Details",font=("Mongolian Baiti",16),bg="white")
        self.DetailsLabel.place(x = 30, y = 160, width="100")

        self.DetailsEntry = Entry(self.mainFrame)
        self.DetailsEntry.place(x = 150, y = 160, width="150",height=30)

        self.DateLabel = Label(self.mainFrame, text="Date",font=("Mongolian Baiti",16),bg="white")
        self.DateLabel.place(x = 28, y = 220, width="100")

        self.joinData = StringVar()
        self.DateEntry = DateEntry(self.mainFrame, textVariable = self.joinData,date_pattern='yyyy-MM-dd')
        self.DateEntry.place(x = 150, y = 220, width="150",height=30)
        
        self.DateEntry.delete(0,'end')
        # self.DateEntry.configure(validate='none')

    
        self.update= Button(self.mainFrame, text = "Update",font=("Mongolian Baiti",16),bg="white", command=self.create)
        self.update.place(x = 50, y = 300)

        # print(f'edit files {database.get_employee(gup)}')
        # self.joinData.set("")

        a = database.get_project(gup)
        self.NameEntry.insert(0,a[1])
        self.DetailsEntry.insert(0,a[3])
        self.DateEntry.insert(0,a[2])
       
        self.root.mainloop()

    def create(self):
        self.data = (
            self.NameEntry.get(),
            self.DateEntry.get(),
            self.DetailsEntry.get(),
            self.Id
        )
        if self.NameEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Name.')
        elif self.DateEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your joining date.')
        elif self.DetailsEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Details.')
        else:
            print("editing",self.data)
            res = database.update_project(self.data)
            if res:
                messagebox.showinfo('Alert','Updated Successfully')
                obj = viewaddproject.viewAddProject(self.root)
                obj.manageTask()
            else:
                messagebox.showinfo('Alert', 'Something went wrong.')






if __name__ == '__main__':
    obj = createEditProject()
    obj.firstFrame('gup')