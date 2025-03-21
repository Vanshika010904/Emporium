import main
import tkinter as tk 
from tkinter import BOTH  
import customtkinter as ctk
import view_user
import pending_user
import addproject
import viewaddproject
import viewaddtask
import addtask
import assigntasks
import viewassigntask
# import reports  # Uncomment if needed

class HomeScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x600")
        self.root.title('Emporium')
        self.root.resizable(False, False)

        self.sidebar_color = '#1f3660'
        options_frame = tk.Frame(self.root, bg=self.sidebar_color)

        # Sidebar Buttons
        self.home_btn = ctk.CTkButton(options_frame, text='Home', font=('Bold', 20), width=20, height=23,
                                       fg_color=self.sidebar_color, command=lambda: self.indicate(self.home_indicate, self.userlist))
        self.home_btn.place(x=10, y=70)
        self.home_indicate = tk.Label(options_frame, text="", bg=self.sidebar_color)
        self.home_indicate.place(x=3, y=70, width=5, height=40)

        self.emp_list = ctk.CTkButton(options_frame, text='Employees', font=('Bold', 20), width=20, height=23,
                                       fg_color=self.sidebar_color, command=lambda: self.indicate(self.emp_indicate, self.userlist))
        self.emp_list.place(x=10, y=120)
        self.emp_indicate = tk.Label(options_frame, text="", bg=self.sidebar_color)
        self.emp_indicate.place(x=3, y=120, width=5, height=40)

        self.pending_user = ctk.CTkButton(options_frame, text='User Request', font=('Bold', 20), width=20, height=23,
                                           fg_color=self.sidebar_color, command=lambda: self.indicate(self.user_indicate, self.pending_req))
        self.pending_user.place(x=10, y=170)
        self.user_indicate = tk.Label(options_frame, text="", bg=self.sidebar_color)
        self.user_indicate.place(x=3, y=170, width=5, height=40)

        self.pro_list = ctk.CTkButton(options_frame, text='Add Project', font=('Bold', 20), width=20, height=23,
                                       fg_color=self.sidebar_color, command=lambda: self.indicate(self.pro_indicate, self.openAddPro))
        self.pro_list.place(x=10, y=220)
        self.pro_indicate = tk.Label(options_frame, text="", bg=self.sidebar_color)
        self.pro_indicate.place(x=3, y=220, width=5, height=40)

        self.man_pro = ctk.CTkButton(options_frame, text='Manage Project', font=('Bold', 20), width=20, height=23,
                                      fg_color=self.sidebar_color, command=lambda: self.indicate(self.man_pro_indicate, self.viewAddPro))
        self.man_pro.place(x=10, y=270)
        self.man_pro_indicate = tk.Label(options_frame, text="", bg=self.sidebar_color)
        self.man_pro_indicate.place(x=3, y=270, width=5, height=40)

        self.task_btn = ctk.CTkButton(options_frame, text='Add Task', font=('Bold', 20), width=20, height=23,
                                       fg_color=self.sidebar_color, command=lambda: self.indicate(self.task_indicate, self.openAddTask))
        self.task_btn.place(x=10, y=320)
        self.task_indicate = tk.Label(options_frame, text="", bg=self.sidebar_color)
        self.task_indicate.place(x=3, y=320, width=5, height=40)

        self.view_task_btn = ctk.CTkButton(options_frame, text='View Tasks', font=('Bold', 20), width=20, height=23,
                                            fg_color=self.sidebar_color, command=lambda: self.indicate(self.view_task_indicate, self.openViewAddTask))
        self.view_task_btn.place(x=10, y=370)
        self.view_task_indicate = tk.Label(options_frame, text="", bg=self.sidebar_color)
        self.view_task_indicate.place(x=3, y=370, width=5, height=40)

        self.assign_task_btn = ctk.CTkButton(options_frame, text='Assign Tasks', font=('Bold', 20), width=20, height=23,
                                              fg_color=self.sidebar_color, command=lambda: self.indicate(self.assign_task_indicate, self.openAddAssignTask))
        self.assign_task_btn.place(x=10, y=420)
        self.assign_task_indicate = tk.Label(options_frame, text="", bg=self.sidebar_color)
        self.assign_task_indicate.place(x=3, y=420, width=5, height=40)

        self.view_assign_task_btn = ctk.CTkButton(options_frame, text='View Assigned Tasks', font=('Bold', 20), width=20, height=23,
                                                   fg_color=self.sidebar_color, command=lambda: self.indicate(self.view_assign_task_indicate, self.openViewAddAssignTask))
        self.view_assign_task_btn.place(x=10, y=470)
        self.view_assign_task_indicate = tk.Label(options_frame, text="", bg=self.sidebar_color)
        self.view_assign_task_indicate.place(x=3, y=470, width=5, height=40)

        self.logoutbtn = ctk.CTkButton(options_frame, text='Logout', font=('Bold', 20), width=20, height=23,
                                                   fg_color=self.sidebar_color, command=lambda: self.indicate(self.logoutbtn_indicate, self.logout))
        self.logoutbtn.place(x=10, y=520)
        self.logoutbtn_indicate = tk.Label(options_frame, text="", bg=self.sidebar_color)
        self.logoutbtn_indicate.place(x=3, y=520, width=5, height=40)

        options_frame.pack(side=tk.LEFT)
        options_frame.pack_propagate(False)
        options_frame.configure(width=210, height=600)

        self.main_frame = tk.Frame(self.root, highlightbackground="black", highlightthickness=1)
        self.main_frame.pack(side=tk.LEFT)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(width=750, height=600)

        # Show user list frame on startup
        self.userlist()
        self.home_indicate.config(bg="white")

        self.root.mainloop()

    def indicate(self, lb, page):
        self.hide_indicators()
        lb.config(bg="white")
        self.delete_frame()
        page()

    def hide_indicators(self):
        indicators = [self.home_indicate, self.emp_indicate, self.user_indicate,
                      self.pro_indicate, self.man_pro_indicate, self.task_indicate,
                      self.view_task_indicate, self.assign_task_indicate, self.view_assign_task_indicate]
        for indicator in indicators:
            indicator.config(bg=self.sidebar_color)

    def userlist(self):
        user_frame = tk.Frame(self.main_frame)
        view_user.showUsers(user_frame)
        user_frame.pack(fill=BOTH, expand=True)

    def pending_req(self):
        user_frame = tk.Frame(self.main_frame)
        pending_user.pendingUserList(user_frame)
        user_frame.pack(fill=BOTH, expand=True)

    def openAddPro(self):
        obj = addproject.createAddProject(self.main_frame)
        obj.firstFrame()

    def viewAddPro(self):
        obj = viewaddproject.viewAddProject(self.main_frame)
        obj.manageTask()

    def openAddTask(self):
        obj = addtask.createAddTask(self.main_frame)
        obj.firstFrame()

    def openViewAddTask(self):
        obj = viewaddtask.viewAddTask(self.main_frame)
        obj.manageTask()

    def openAddAssignTask(self):
        obj = assigntasks.createAddTask(self.main_frame)
        obj.firstFrame()

    def openViewAddAssignTask(self):
        obj = viewassigntask.viewAssignTask(self.main_frame)
        obj.manageTask()

    def logout(self):
        # Destroy the current HomeScreen window
        self.root.destroy()
        # Create an instance of the Main class to go back to the login screen
        main.Main()

    def delete_frame(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()

if __name__ == "__main__":
    HomeScreen()
