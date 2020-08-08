from tkinter import *        #import modules
import os                      # To interect with our operating system

#designing window for registration

def register():
    global reg_screen
    reg_screen = Toplevel(screen)
    reg_screen.title("Register")
    reg_screen.geometry("300x250")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(reg_screen,text="enter detail below",bg="light blue").pack()
    Label(reg_screen, text="").pack()
    username_lable = Lable(reg_screen, textvariable="username")
    username_lable.pack()
    username_entry = Entry(reg_screen, textvariable=username)
    username_entry.pack()
    password_lable = Lable(reg_screen, textvariable="password")
    password_lable.pack()
    password_entry = Entry(reg_screen, textvariable=password, show="*")
    password_entry.pack()
    Button(reg_screen, text="Register",width=10,height=1,bg="blue",command=reg_usr).pack()
    
 #design for login
def login():
    global login_screen
    login_screen = Toplevel(screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    
   Label(login_screen,text="enter detail for login the user").pack()
    
    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry

    username_verify=StringVar()
    password_verify=StringVar()
    
    
    Label(login_screen,text="uername").pack()
    usrename_login_entry=Entry(login_screen,textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen,text="password").pack()
    password_login_entry=Entry(login_screen, textvariable=password_verify,show="*")
    password_login_entry.pack()
    Label(login_screen,text="").pack()
    Button(login_screen,text="Login",width=11,height=1,command=login_verify).pack()
    
     #work on register button

def reg_user():
    username_info=username.get()
    password_info=password.get()


    file=open(username_info, "w")             #file open in wrie mode
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()                  #close the file
    usrename.entry.delete(0,END)
    password_entry.delete(0,END)

    Label(register_screen,text="Registration Success",fg="green",font=("calibri",11)).pack()
        
        #work on login button
def login_verify():
    username1=username_verify.get()     #get username and password
    password1=password_verify.get()

    username_login_entry.delete(0,END)
    password_login_entry.delete(0,END)       #this ll delete the entry after press the login button
    list_of_files = os.listdir()            #The method listdir() returns a list containing the names of the entries in the directory given by path.
    
    if username1 in list_of_files:
        file1 = open(username1, "r")       #open the file in read mode
        verify=file1.read().splitlines()   # It breaks the string at line boundaries and returns a list of splitted strings
        if password1 in verify:  
              login_sucess()

        else:
             password_not_recognised()
    else:
          user_not_found()
            
            #FOR LOGIN_SUCESS FUNCTION

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen,text="Login success").pack()
    Button(login_success_screen,text="Ok", command=delete_login_success).pack()
    
    #FOR INVALID PSSWORD
def password_not_recognised():
    global password_not_rec_screen
    password_not_rec_screen = Toplevel(screen)
    password_not_rec_screen.title("Success")
    password_not_rec_screen.geometry("150x100")
    Label(password_not_rec_screen,text="Invalid Password").pack()
    Button(password_not_rec_screen,text="Ok",command=delete_password_not_recognised).pack()
    
    #DESIGN FOR USER NOT FOUND
def user_not_found():
    global user_not_found_screen
    user_not_found_screen=Toplevel(screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen,text="user Not Found").pack()
    Button(user_not_found_screen,text="Ok",command=delete_user_not_found_screen).pack()
    
     #DELETING POUPS

def delete_login_success():                        
    login_success_screen.destroy()

def delete_password_not_recognised():
    password_not_rec_screen.destroy()
    
def delete_user_not_found_screen():      # now define a function for deleting this popup. and here is  the code.    
    user_not_found_screen.destroy

            



