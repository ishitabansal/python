import tkinter as tk
from tkinter import ttk   #import the tkinter

expr=" "          # create global variable

def press(num):        #create function press
    global expr
    expr=expr+str(num)             #converting string
    eq.set(expr)    #update expression using set method


def press1():     #function name equalpress
    try:
        global expr      #global variable
        ttl = str(eval(expr))        #eval function expression evaluate krega and str convert into the string
        eq.set(ttl)                    #dispplay the total number

        expr = " "                          #show expression and initialize the expression by empty string
    except:
        eq.set("ERROR")           #show the error msg
        expr = " "   
        
 
def clear():                          #clear the expression. clear is function name
    global expr
    expr = " "
    eq.set(" ")


if __name__ == "__main__":     #main program
    top = tk.Tk()              #define top
    top.title("Calculator")     #Title name name
    top.iconbitmap("Images.jpg")        #set Icon
    top.geometry("260x172")
    top.maxsize(width=260,height=170)           #max size
    top.configure(bg="green")

        
        
