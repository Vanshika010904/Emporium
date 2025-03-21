
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import ttk

from PIL import Image, ImageTk
# import viewaddemployee
import viewaddproject
import sidebar
import database

class createAddProject:

    # constructor
    def __init__(self,window):
        self.root = window
        

    def firstFrame(self):

        # create a frame
        self.mainFrame = Frame(self.root,bg="white")
        self.mainFrame.place(x = 0, y = 0, width="800", height="500")

        self.my_label=Label(self.mainFrame,text="Project Details",font=("Mongolian Baiti",20),bg="white")
        self.my_label.place(x=50,y=30,width="270")
                        
        # self.backBtn=Button(self.mainFrame,text="Back",font=("Mongolian Baiti",16),bg="white", command= self.back)
        # self.backBtn.place(x=230,y=250,width="70",height=40)

        # set background image
        
        self.image = ImageTk.PhotoImage(Image.open('empimg1.jpg'))
        self.bgLabel = Label(self.mainFrame, image=self.image)
        self.bgLabel.place(x = 350, y =  0,  width="450", height = "500")


        self.NameLabel = Label(self.mainFrame, text="Name",font=("Mongolian Baiti",16),bg="white")
        self.NameLabel.place(x = 30, y = 100, width="100")

        self.NameEntry = Entry(self.mainFrame)
        self.NameEntry.place(x = 150, y = 100, width="150",height=30)

        self.DetailsLabel = Label(self.mainFrame, text="Details",font=("Mongolian Baiti",16),bg="white")
        self.DetailsLabel.place(x = 36, y = 160, width="100")

        self.DetailsEntry = Entry(self.mainFrame)
        self.DetailsEntry.place(x = 150, y = 160, width="150",height=30)

        # self.dateLabel = Label(self.mainFrame, text="Date",font=("Mongolian Baiti",16),bg="white")
        # self.dateLabel.place(x = 28, y = 220, width="100")

        # self.joinData = StringVar()
        # self.dateEntry = DateEntry(self.mainFrame, textVariable = self.joinData)
        # self.dateEntry.place(x = 150, y = 220, width="150",height=30)
    
        self.submit = Button(self.mainFrame, text = "Submit",font=("Mongolian Baiti",16),bg="white", command=self.create)
        self.submit.place(x = 150, y = 250)

        self.root.mainloop()

    def create(self):
        self.data = [
            # self.ProIDEntry.get(), 
            self.NameEntry.get(),  
            # self.dateEntry.get(),
            self.DetailsEntry.get()
        ]
        # if (self.ProIDEntry.get() == ''):
        #     messagebox.showinfo('Alert', 'Enter your ProID.')
        # elif(self.ProIDEntry.get().isalpha()):
        #     messagebox.showinfo('alert','enter valid EmpId')
        if self.NameEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Name.')
        elif self.DetailsEntry.get() == '':
            messagebox.showinfo('Alert', 'Enter your Details.')
        # elif self.dateEntry.get() == '':
        #     messagebox.showinfo('Alert', 'Enter your  date.')
        else:
            res = database.addPro(self.data)
            if res:
                messagebox.showinfo('Alert','Submitted Successfully')
                # obj = viewaddproject.viewAddProject(self.root)
                self.NameEntry.delete(0,END)
                self.DetailsEntry.delete(0,END)
                
                # obj.manageTask()
            else:
                messagebox.showinfo('Alert', 'Something went wrong.')



if __name__ == '__main__':
    obj = createAddProject()
    obj.firstFrame()