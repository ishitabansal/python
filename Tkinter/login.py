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



