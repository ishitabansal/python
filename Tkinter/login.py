from tkinter import *        #import modules
import os                      # To interect with our operating system

#designing window for registration

def register():
    global reg_screen
    reg_screen = Toplevel(screen)
    reg_screen.title("Register")
    reg_screen.geometry("300x250")
