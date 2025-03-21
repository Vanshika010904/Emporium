import mysql.connector

try:
    db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        db = 'emp'
    )
    print("Connected successfully")
except Exception as e:
    print("Dataabase not connected: ",e)

cursor = db.cursor()



def registerUser(data):
    try:
        cursor.execute('INSERT into pendinguser(name,email,dept,dob,date) Values(%s,%s,%s,%s,%s)',data)
        print("data in the fun",data)
        db.commit()
        return True
    except Exception as e:
        print("Error is in register user :", e)
        return False
    

def allUsers():
    try:
        cursor.execute('Select * from employees')
        return cursor.fetchall()
    except Exception as e:
        print("Error in all user :",e)

def allPendingUsers():
    try:
        cursor.execute('Select * from pendinguser')
        return cursor.fetchall()
    except Exception as e:
        print("Error in all user :",e)


def loginUserEmail(data):
    try:    
        cursor.execute('Select * from employees where email = %s and password = %s',data)
        return cursor.fetchone()
    except Exception as e:
        print("Error in login user:" , e)
        return False
    
def loginUserUsername(data):
    try:
        cursor.execute('Select * from employees where name = %s and password = %s',data)
        return cursor.fetchone()
    except Exception as e:
        print("Error in login user: ",e)
        return False
    
def loginAdminEmail(data):
    try:    
        cursor.execute('Select * from admin where email = %s and password = %s',data)
        return cursor.fetchone()
    except Exception as e:
        print("Error in login user:" , e)
        return False
    
def loginAdminUsername(data):
    try:
        cursor.execute('Select * from admin where name = %s and password = %s',data)
        return cursor.fetchone()
    except Exception as e:
        print("Error in login user: ",e)
        return False


def deleteUser(id):
    try:
        cursor.execute('Delete from  employees where id=%s',id)
        db.commit()
        return True
    except Exception as e:
        print("Error is ----",e)
        return False
    
def deletePendingUser(id):
    try:
        cursor.execute('Delete from  pendingUser where id=%s',id)
        db.commit()
        return True
    except Exception as e:
        print("Error is ----",e)
        return False   

def getSingleUser(id):
    try:
        cursor.execute('select * from employees where id=%s',id)
        return cursor.fetchone()
    except Exception as e:
        print("Error is ",e)
        return False
    
def updateUser(data):
    try:
        print(data)
        cursor.execute('update employees set name=%s, email=%s, password=%s where id=%s',data)
        db.commit()
        return True
    except Exception as e:
        print("Error----",e)
        return False


def getSinglePendingUser(id):
    try:
        cursor.execute('select * from pendingUser where id=%s',id)
        return cursor.fetchone()
    except Exception as e:
        print("Error is ",e)
        return False

def task(data):
    try:
        cursor.execute('INSERT into task1(task_name,description,pending,name) Values(%s,%s,%s,%s)',data)
        print("data in the fun",data)
        db.commit()
        return True
    except Exception as e:
        print(data)
        print("Error is :", e)
        return False



def addEmployee(data):
    try:
        cursor.execute('INSERT into employees(name,email,password,dob,dept,profile,time,username) Values(%s,%s,%s,%s,%s,%s,%s,%s)',data)
        print("data in the fun",data)
        db.commit()
        return True
    except Exception as e:
        print(data)
        print("Error is :", e)
        return False

def addemployeeLogin(arg):
    print(arg)
    # cursor.execute("SELECT * FROM addemployee WHERE email =%sand password =%s", arg)

    try:
        cursor.execute("SELECT * FROM employees WHERE Email =%s and Password =%s", arg)
        return cursor.fetchone()
    except:
        return False
def addPro(arg):
    
    try:
        print(arg)
        cursor.execute("INSERT INTO addproject (ProName, details) VALUES (%s,%s)", arg)
        db.commit()
        return True
    except:
        return False


def addtask(arg):
    try:
        # print(arg)
        cursor.execute("INSERT INTO tasks (projectId,name) VALUES (%s,%s)", arg)
        db.commit()
        return True
    except:
        return []

def assigntask(arg):
    try:
        emp_id = arg[0]  # Assuming EmpId is the first element in arg
        
        # Check if EmpId exists in the employees table
        cursor.execute("SELECT id FROM employees WHERE id = %s", (emp_id,))
        if cursor.fetchone() is None:
            print(f"EmpId {emp_id} does not exist in employees.")
            return []

        print("Attempting to insert with values:", arg)
        cursor.execute(
            "INSERT INTO assigntask (EmpId, taskId, Startdate, Enddate, Status) VALUES (%s, %s, %s, %s, %s)", 
            arg
        )
        db.commit()
        return True
    except Exception as e:
        print("Error in assign task", e)
        return []


def allEmployees():
    try:
        cursor.execute("SELECT * FROM employees")
        return cursor.fetchall()
    except:
        return False
    
def allProjects():
    try:
        cursor.execute("SELECT * FROM addproject")
        return cursor.fetchall()
    except:
        return False

def allTask():
    # cursor.execute("SELECT * FROM addtask")

    try:
        cursor.execute("SELECT tasks.id,addproject.ProName,tasks.name FROM tasks inner join addproject on addproject.id=tasks.projectId")
        return cursor.fetchall()
    except:
        return []

def allassignTask():
    try:
        cursor.execute("SELECT assigntask.id,employees.name, tasks.name, assigntask.Startdate, assigntask.Enddate, assigntask.Status FROM assigntask left join employees on employees.id = assigntask.EmpId left join tasks on tasks.id = assigntask.taskId")
        return cursor.fetchall()
    except:
        return []


def allFeedback():
    try:
        cursor.execute("SELECT * FROM feedback")
        return cursor.fetchall()
    except:
        return False

def deleteEmp(id):
    try:
        cursor.execute("DELETE FROM addemployee WHERE id = %s", id)
        db.commit()
        return True
    except:
        return False

def deleteAssignedTask(task_id):
    try:
        cursor.execute("DELETE FROM assigntask WHERE id = %s",(task_id,))  # Pass as a tuple
        db.commit()  # Commit the changes
        return True  # Return True on success
    except Exception as e:
        print(f"error in assign task Error: {e}")  # Log the error message
        return False  # Return False if there was an error
    
def deleteTask(task_id):
    try:
        # Ensure task_id is of the correct type
        if not isinstance(task_id, int):
            raise ValueError("task_id must be an integer")
        
        # Execute the query with parameterized query
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        
        # Commit the changes
        db.commit()
        return True  # Return True on success
    except Exception as e:
        print(f"Error in deleteTask: {e}")  # Log the error message
        return False  # Return False if there was an error



def deleteProject(id):
    try:
        cursor.execute("DELETE FROM addproject WHERE id = %s", id)
        db.commit()
        return True
    except:
        return False

def get_employee(gup):
    try:
        print('get',gup)
        cursor.execute("SELECT * FROM employees WHERE id=%s",gup)
        return cursor.fetchone()
    except:
        return False

def get_project(gup):
    try:
        print('get',gup)
        cursor.execute("SELECT * FROM addproject WHERE id=%s",gup)
        return cursor.fetchone()
    except:
        return False

def get_assigntask(gup):
    try:
        print('get', gup)
        cursor.execute(
            "SELECT employees.id, employees.name, tasks.name, assigntask.Startdate, assigntask.Enddate, assigntask.Status, tasks.id "
            "FROM assigntask "
            "LEFT JOIN employees ON employees.id = assigntask.EmpId "
            "LEFT JOIN tasks ON tasks.id = assigntask.taskId "
            "WHERE assigntask.id = %s", 
            (gup,)  # Pass gup as a tuple
        )
        return cursor.fetchone()
    except Exception as e:
        print("Error in assign Task", e)
        return False

def update_employee(gup):
    try:
        print('get hello',gup)
        cursor.execute(" UPDATE addemployee SET EmpId=%s,Name=%s,Email=%s,Password=%s,Contact=%s,Address=%s,DOJ=%s WHERE Id=%s",gup)
        db.commit()
        return True
    except:
        return False

def update_project(gup):
    try:
        print('get hello',gup)
        cursor.execute(" UPDATE addproject SET ProName=%s,date=%s,details=%s WHERE id=%s",gup)
        db.commit()
        return True
    except:
        return False

def update_assigntask(gup): 
    try:
        print("Updating assign task with values:", gup)

        # Extract values from the input tuple
        EmpId, taskId, Startdate, Enddate, Status, id = gup

        # Ensure taskId is an integer, if not try to convert it
        if not isinstance(taskId, int):
            try:
                taskId = int(taskId)
            except ValueError:
                print(f"Error: taskId {taskId} is not a valid integer.")
                return False

        # Validate EmpId exists in the addemployee table
        cursor.execute("SELECT id FROM addemployee WHERE id = %s", (EmpId,))
        emp_result = cursor.fetchone()
        if not emp_result:
            print(f"Error: EmpId {EmpId} does not exist in the addemployee table.")
            return False

        # Validate taskId exists in the tasks table
        cursor.execute("SELECT id FROM tasks WHERE id = %s", (taskId,))
        task_result = cursor.fetchone()
        if not task_result:
            print(f"Error: taskId {taskId} does not exist in the tasks table.")
            return False

        # Perform the update
        cursor.execute(
            """
            UPDATE assigntask 
            SET EmpId=%s, taskId=%s, Startdate=%s, Enddate=%s, Status=%s 
            WHERE id=%s
            """,
            gup
        )
        db.commit()
        print("Update successful!")
        return True

    except Exception as e:
        print("Error in update_assigntask------", e)
        db.rollback()  # Rollback in case of an error
        return False



def get_id_of_task(data):
    try:
        cursor.execute("SELECT id FROM tasks WHERE name = %s", (data,))
        result = cursor.fetchone()  # Fetch the result
        if result:
            return result[0]  # Return the id if found
        else:
            return None  # Return None if no task is found
    except Exception as e:
        print("Error in fun get_id_of_task line 381:", e)
        return None




def get_task(gup):
    try:
        print('get',gup)
        cursor.execute("SELECT addproject.id, addproject.ProName, tasks.name FROM tasks left join addproject on addproject.id = tasks.projectId WHERE tasks.id = %s", gup)
        return cursor.fetchone()
    except:
        return []


def update_task(gup):
    try:
        print('get',gup)
        cursor.execute(" UPDATE tasks SET projectId=%s,name=%s WHERE id=%s",gup)
        db.commit()
        return True
    except:
        return []


# def nameEmp():
#     try:
#         cursor.execute('SELECT id,Name from addemployee')
#         return cursor.fetchall()
#     except:
#         return False

def nameEmp():
    try:
        cursor.execute('SELECT id,name from employees')
        return cursor.fetchall()
    except:
        return False

def namePro():
    try:
        cursor.execute('SELECT id,ProName from addproject')
        return cursor.fetchall()
    except:
        return False

def nameTask():
    try:
        cursor.execute('SELECT id,name from tasks')
        return cursor.fetchall()
    except:
        return False
        


def pendingTask():
    try:
        cursor.execute('SELECT * from assigntask WHERE status = "pending"')
        return cursor.fetchall()
    except:
        return []

def completedTask():
    try:
        cursor.execute('SELECT * from assigntask WHERE status = "completed"')
        return cursor.fetchall()
    except:
        return []

def ReportTask(val):
    try:
        cursor.execute("SELECT * from tasks where projectId = %s", (val,))
        return cursor.fetchall()
    except:
        return []

def reportassignTask(val):
    print("value in db ",val)
    try:
        cursor.execute("SELECT assigntask.id,addemployee.Name, tasks.name, assigntask.Startdate, assigntask.Enddate, assigntask.Status FROM assigntask left join addemployee on addemployee.id = assigntask.EmpId left join tasks on tasks.id = assigntask.taskId WHERE assigntask.taskId = %s",(val,))
        return cursor.fetchall()
    except:
        return []
    
def employeeLogin(arg):
    print(arg)
    # cursor.execute("SELECT * FROM addemployee WHERE email =%sand password =%s", arg)

    try:
        cursor.execute("SELECT * FROM addemployee WHERE Email =%s and Password =%s", arg)
        return cursor.fetchone()
    except:
        return False

def userallTask():
    try:
        cursor.execute("SELECT * FROM tasks")
        cursor.fetchall()
        return True
    except:
        return False


def getEmpName(email):
    try:
        cursor.execute('SELECT id from employees WHERE email = %s', (email, ))
        return cursor.fetchone()
    except:
        return False

def allPendingEmpTask(data):
    try:
        cursor.execute('SELECT assigntask.id, employees.Name, tasks.name, assigntask.Startdate, assigntask.Enddate, assigntask.Status FROM assigntask inner join employees on employees.id = assigntask.EmpId left join tasks on tasks.id = assigntask.taskId WHERE employees.id = %s and assigntask.Status = "pending"', data)
        return cursor.fetchall()
    except:
        return []


def allCompletedEmpTask(data):
    try:
        cursor.execute('SELECT assigntask.id, employees.name, tasks.name, assigntask.Startdate, assigntask.Enddate, assigntask.Status FROM assigntask inner join employees on employees.id = assigntask.EmpId left join tasks on tasks.id = assigntask.taskId WHERE employees.id = %s and assigntask.Status = "completed"', data)
        return cursor.fetchall()
    except:
        return []

def allEmpTask(data):
    try:
        # Ensure `data` is passed as a tuple
        print("data in allEmp task=====",data)
        cursor.execute('''
            SELECT assigntask.id, employees.name, tasks.name, 
                   assigntask.Startdate, assigntask.Enddate, assigntask.Status 
            FROM assigntask 
            INNER JOIN employees ON employees.id = assigntask.EmpId 
            LEFT JOIN tasks ON tasks.id = assigntask.taskId 
            WHERE employees.id = %s
        ''', (data,))  # Ensure `data` is wrapped in a tuple

        # Fetch all results
        result = cursor.fetchall()
        print("Fetched data:", result)  # Optional debug print
        return result
    except Exception as e:
        print("Error in allEmpTask ---", e)
        return []


def completeTask(arg):
    try:
        cursor.execute('UPDATE assigntask SET Status = "completed" WHERE id = %s ', arg)
        db.commit()
        return True
    except:
        return []

def completeProject(arg):
    try:
        cursor.execute('UPDATE assigntask SET Status = "completed" WHERE id = %s ', arg)
        db.commit()
        return True
    except:
        return []

def addFeedbacks(arg):
    try:
        cursor.execute('INSERT INTO feedback (TaskName, EmpId, Feedback) VALUES (%s, %s, %s)', arg)
        db.commit()
        return True
    except:
        return False


def allEmpTaskName(data):
    try:
        cursor.execute('SELECT tasks.name FROM assigntask left join employees on employees.id = assigntask.EmpId left join tasks on tasks.id = assigntask.taskId WHERE employees.name = %s ', data)
        return cursor.fetchall()
    except:
        return False

def allEmpName(data):
    try:
        cursor.execute('SELECT employees.Name FROM assigntask left join employees on employees.id = assigntask.EmpId left join tasks on tasks.id = assigntask.taskId WHERE employees.name = %s ', data)
        return cursor.fetchall()
    except:
        return False

def allFeedback(args):
    try:
        cursor.execute('SELECT * FROM feedback WHERE EmpId = %s', args)
        return cursor.fetchall()
    except:
        return False
        
def allEmpProject(data):
    try:
        cursor.execute('SELECT assigntask.id, employees.name, tasks.name,addproject.ProName, assigntask.Startdate, assigntask.Enddate, assigntask.Status, addproject.id FROM assigntask left join employees on employees.id = assigntask.EmpId left join tasks on tasks.id = assigntask.taskId left join addproject on addproject.id=tasks.projectId WHERE employees.id = %s ', data)
        return cursor.fetchall()
    except:
        return []

def allCompletedEmpProject(data):
    try:
        cursor.execute('SELECT assigntask.id, employees.name, tasks.name,addproject.ProName, assigntask.Startdate, assigntask.Enddate, assigntask.Status FROM assigntask left join employees on employees.id = assigntask.EmpId left join tasks on tasks.id = assigntask.taskId left join addproject on addproject.id=tasks.projectId WHERE employees.name = %s and assigntask.Status = "completed"', data)
        return cursor.fetchall()
    except:
        return []

def allPendingEmpProject(data):
    try:
        cursor.execute('SELECT assigntask.id, employees.Name, tasks.name,addproject.ProName, assigntask.Startdate, assigntask.Enddate, assigntask.Status FROM assigntask left join employees on employees.id = assigntask.EmpId left join tasks on tasks.id = assigntask.taskId left join addproject on addproject.id=tasks.projectId WHERE employees.Name = %s and assigntask.Status = "pending"', data)
        return cursor.fetchall()
    except:
        return []