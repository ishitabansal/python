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

