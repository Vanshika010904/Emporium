#user screen
import main
from tkinter import*
from PIL import Image,ImageTk

import viewalltask
import viewpendingtask
import viewcompletedtask
# import addfeedback
import viewfeedback
import openProjectTask

import database


class createEmphomemenu:

    # constructor
    def __init__(self,data, status):
        self.root = Tk()
        self.root.title('Home Menu')
        self.root.resizable(height=False,width=False)
        self.root.geometry("900x600")
        self.data = data
        self.status = status
        
        self.firstFrame()
        self.root.mainloop()

       
    def firstFrame(self):
        
        # print(f'frame {self.data}')
        # print(self.data,"----------------------------------------")
        if self.status == 'login':
            self.empName = database.getEmpName(self.data)
            print("se.empName--",self.empName)
            # tmp = database.allEmpTask
            # print("-------------------------------",tmp)
        else:
            self.empName = self.data[0]
        print(self.empName)
        # create a frame
        self.mainFrame = Frame(self.root,bg="white")
        self.mainFrame.place(x = 0, y = 0, width="800", height="500")

       
        # set background image
        self.image = ImageTk.PhotoImage(Image.open('empmenu1.jpg'))
        self.bgLabel = Label(self.mainFrame, image=self.image)
        self.bgLabel.place(x = 300 , y = 0,  width="600", height = "500")

        
    
        menubar=Menu(self.mainFrame)



        self.my_label=Label(self.root,text="TASKS",font=("Mongolian Baiti",20),bg="white")
        self.my_label.place(x=25,y=30,width="170")

        self.TaskLabel = Label(self.mainFrame, text="All Tasks",font=("Mongolian Baiti",16))
        self.TaskLabel.place(x = 10, y = 100, width="100")

        self.TasknoLabel = Label(self.mainFrame, text=len(database.allEmpTask(self.empName[0])),font=("Mongolian Baiti",16))
        self.TasknoLabel.place(x = 130, y = 100, width="30")

        self.PendingLabel = Label(self.mainFrame, text="Pending",font=("Mongolian Baiti",16))
        self.PendingLabel.place(x = 10, y = 150, width="100")

        self.PendingLabel = Label(self.mainFrame, text=len(database.allPendingEmpTask(self.empName)),font=("Mongolian Baiti",16))
        self.PendingLabel.place(x = 130, y = 150, width="30")

        self.CompletedLabel = Label(self.mainFrame, text="Completed",font=("Mongolian Baiti",16))
        self.CompletedLabel.place(x = 15, y = 200, width="100")

        self.CompletedLabel = Label(self.mainFrame, text=len(database.allCompletedEmpTask(self.empName)),font=("Mongolian Baiti",16))
        self.CompletedLabel.place(x = 130, y = 200, width="30")

        #adding self.task menu and commands
        task=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Task",menu=task)
        task.add_command(label="All Tasks",command=self.openViewAllTask)
        # task.add_command(label="Pending Tasks",command=self.openViewPendingTask)
        # task.add_command(label="Completed Tasks",command=self.openViewCompletedTask)


        project=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Project",menu=project)
        dat = database.allEmpProject(self.empName)
        print("Data in dat", dat)
        taskDic = dict()
        for i in dat:
            if i[3] not in taskDic.keys():
                taskDic[i[3]] = []
            if i[3] in taskDic.keys():
                taskDic.get(i[3]).append(i)
       
        # dat = list(set(dat))
        # print(" value ",dat)
        for i in taskDic.keys():
            print(i)
            project.add_command(label=i, command= lambda x=i: self.openProjectTask(taskDic[x]))

        menubar.add_command(label='logout',command=self.logout)
        self.root.config(menu=menubar)
    
    def logout(self):
        # Destroy the current HomeScreen window
        self.root.destroy()
        # Create an instance of the Main class to go back to the login screen
        main.Main()

    def openProjectTask(self,data):
        # print("hello",data)
        # self.root.destroy()
        obj = openProjectTask.openProjectTask()
        obj.manageProject(self.empName,data)
        

    def openViewAllTask(self):
        # self.root.destroy()
        obj = viewalltask.viewAddTask()
        obj.manageTask(self.empName)
        
    # def openViewPendingTask(self):
    #     self.root.destroy()
    #     obj = viewpendingtask.viewAddTask()
    #     obj.manageTask(self.empName)
    
    # def openViewCompletedTask(self):
    #     self.root.destroy()
    #     obj = viewcompletedtask.viewAddTask()
    #     obj.manageTask(self.empName)
        
    # def openViewAddFeedback(self):
    #     self.root.destroy()
    #     obj = addfeedback.createAddFeedback()
    #     obj.firstFrame(self.empName)

    # def openViewFeedback(self):
    #     self.root.destroy()
    #     obj = viewfeedback.viewFeedback()
    #     obj.manageFeedback(self.empName)
        
    
if __name__=="__main__":
     obj=createEmphomemenu()
     obj.firstFrame()



# from tkinter import *
# from PIL import Image, ImageTk

# import viewalltask
# import viewpendingtask
# import viewcompletedtask
# import viewfeedback
# import openProjectTask
# import database


# class CreateEmpHomeMenu:
#     def __init__(self,data,status):
#         self.data=data
#         self.status=status
#         self.root = Tk()
#         self.root.title('Home Menu')

#         # Get the width and height of the screen
#         self.fullwidth = self.root.winfo_screenwidth()
#         self.fullheight = self.root.winfo_screenheight()

#         # Set the size and position of the window
#         self.width = int((self.fullwidth - 900) / 2)
#         self.height = int((self.fullheight - 600) / 2)
#         self.root.geometry(f"800x500+{self.width}+{self.height}")

#         # Disable resizing of the window
#         self.root.resizable(height=False, width=False)

#     def first_frame(self):
       
#         self.empName = database.getEmpName(self.data) if self.status == 'login' else self.data

#         self.main_frame = Frame(self.root, bg="white")
#         self.main_frame.place(x=0, y=0, width="800", height="500")

#         self.set_background_image()
#         self.create_widgets()
#         self.setup_menubar()
#         # Mlabel = Label(self.root,text="Testing",font=("Arial",20,"bold")) 


#     def set_background_image(self):
#         self.image = ImageTk.PhotoImage(Image.open('empmenu1.jpg'))
#         self.bg_label = Label(self.main_frame, image=self.image)
#         self.bg_label.place(x=300, y=0, width="600", height="500")

#     def create_widgets(self):
#         Label(self.root, text="TASKS", font=("Mongolian Baiti", 20), bg="white").place(x=25, y=30, width="170")

#         self.create_task_label("All Tasks", 10, 100, database.allEmpTask(self.empName))
#         self.create_task_label("Pending", 10, 150, database.allPendingEmpTask(self.empName))
#         self.create_task_label("Completed", 15, 200, database.allCompletedEmpTask(self.empName))

#     def create_task_label(self, text, x, y, task_count):
#         Label(self.main_frame, text=text, font=("Mongolian Baiti", 16)).place(x=x, y=y, width="100")
#         Label(self.main_frame, text=len(task_count), font=("Mongolian Baiti", 16)).place(x=x+120, y=y, width="30")

#     def setup_menubar(self):
#         menubar = Menu(self.main_frame)

#         # Task menu
#         task_menu = Menu(menubar, tearoff=0)
#         menubar.add_cascade(label="Task", menu=task_menu)
#         task_menu.add_command(label="All Tasks", command=self.open_view_all_task)
#         # Uncomment these if the methods are implemented
#         # task_menu.add_command(label="Pending Tasks", command=self.open_view_pending_task)
#         # task_menu.add_command(label="Completed Tasks", command=self.open_view_completed_task)

#         # Project menu
#         project_menu = Menu(menubar, tearoff=0)
#         menubar.add_cascade(label="Project", menu=project_menu)
#         self.populate_project_menu(project_menu)

#         menubar.add_command(label='Logout', command=self.root.quit)
#         self.root.config(menu=menubar)

#     def populate_project_menu(self, project_menu):
#         projects = database.allEmpProject(self.empName)
#         task_dict = {}

#         for project in projects:
#             project_name = project[3]
#             if project_name not in task_dict:
#                 task_dict[project_name] = []
#             task_dict[project_name].append(project)

#         for project_name in task_dict:
#             project_menu.add_command(label=project_name, command=lambda p=task_dict[project_name]: self.open_project_task(p))

#     def open_project_task(self, data):
#         obj = openProjectTask.OpenProjectTask()
#         obj.manage_project(self.empName, data)

#     def open_view_all_task(self):
#         self.root.destroy()
#         obj = viewalltask.ViewAllTask()
#         obj.manage_task(self.empName)

#     # Uncomment these methods if you need them
#     # def open_view_pending_task(self):
#     #     self.root.destroy()
#     #     obj = viewpendingtask.ViewPendingTask()
#     #     obj.manage_task(self.empName)

#     # def open_view_completed_task(self):
#     #     self.root.destroy()
#     #     obj = viewcompletedtask.ViewCompletedTask()
#     #     obj.manage_task(self.empName)

#     # def open_view_feedback(self):
#     #     self.root.destroy()
#     #     obj = viewfeedback.ViewFeedback()
#     #     obj.manage_feedback(self.empName)


# if __name__ == "__main__":
#     obj = CreateEmpHomeMenu()
#     obj.first_frame(['dummy_employee_id'], 'login')  # Replace with actual data and status
