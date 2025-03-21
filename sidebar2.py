import tkinter as tk
import task_pending
import task_done
import database
from PIL import Image,ImageTk
import io
class sidebar1:
   def __init__(self,data) :
        print(data)
        passed_data=data
        self.root=tk.Tk()
        self.root.geometry('500x400')
        self.root.title('tkinter hub')
        res = database.getSingleUser((passed_data,))
        print(res)
        image = Image.open(io.BytesIO(res[6]))
        image = image.resize((200, 200), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(image)


        self.options_frame=tk.Frame(self.root,bg='#353f66')


        self.home_btn=tk.Button(self.options_frame,text='HOME',font=('Bold',15),fg='#d3d7e6',bd=0,bg='#353f66',command=lambda:self.indicate(self.home_indicator,self.home_page))
        self.home_btn.place(x=10,y=50)
        self.home_indicator=tk.Label(self.options_frame,text='',bg='#353f66')
        self.home_indicator.place(x=3,y=50,width=5,height=40)


        self.task_pending_btn=tk.Button(self.options_frame,text='TASK',font=('Bold',15),fg='#d3d7e6',bd=0,bg='#353f66',command=lambda:self.indicate(self.task_indicator,self.task_pen))
        self.task_pending_btn.place(x=10,y=100)
        self.task_indicator=tk.Label(self.options_frame,text='',bg='#353f66')
        self.task_indicator.place(x=3,y=100,width=5,height=40)




        self.done_btn=tk.Button(self.options_frame,text='DONE',font=('Bold',15),fg='#d3d7e6',bd=0,bg='#353f66',command=lambda:self.indicate(self.done_indicator,self.task_done))
        self.done_btn.place(x=10,y=150)
        self.done_indicator=tk.Label(self.options_frame,text='',bg='#353f66')
        self.done_indicator.place(x=3,y=150,width=5,height=40)



        self.options_frame.pack(side=tk.LEFT)
        self.options_frame.pack_propagate(False)
        self.options_frame.configure(width=100,height=400)

        self.main_frame=tk.Frame(self.root,highlightbackground='black',highlightthickness=2)
        self.main_frame.pack(side=tk.LEFT)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(height=400,width=500)

        self.task_pen()
        self.root.mainloop()


   def home_page(self):
       self.home_frame=tk.Frame(self.main_frame)
    #    self.lb=(tk.Label(self.home_frame,text='Home Page\n\nPage:1',font=('Bold',30)))
       self.lb=(tk.Label(self.home_frame,image= self.image))
       self.lb.pack()
       self.home_frame.pack(pady=20)

#    def task_page(self):
#        self.task_frame=tk.Frame(self.main_frame)
#        self.lb=(tk.Label(self.task_frame,text='task Page\n\nPage:2',font=('Bold',30)))
#        self.lb.pack()
#        self.task_frame.pack(pady=20)

#    def done_page(self):
#        self.done_frame=tk.Frame(self.main_frame)
#        self.lb=(tk.Label(self.done_frame,text='Home Page\n\nPage:3',font=('Bold',30)))
#        self.lb.pack()
#        self.done_frame.pack(pady=20)


   def hide_indicators(self):
    self.home_indicator.config(bg='#353f66')
    self.task_indicator.config(bg='#353f66')
    self.done_indicator.config(bg='#353f66')



   def indicate(self,lb,page):
    self.hide_indicators()
    lb.config(bg='#d3d7e6')
    self.delete_pages()
    page()

   def task_pen(self):
       user_frame = tk.Frame(self.main_frame)
       task_pending.Task(user_frame)
       user_frame.pack(fill='both', expand=True)

       
   def task_done(self):
       user_frame = tk.Frame(self.main_frame)
       task_done.Task(user_frame)
       user_frame.pack(fill='both', expand=True)



   def delete_pages(self):
    for frame in self.main_frame.winfo_children():
        frame.destroy()

   def delete_frame(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()


if __name__=="__main__":
   sidebar1(8)