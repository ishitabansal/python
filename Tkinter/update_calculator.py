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
    top.configure(bg="red")
    
  #create the entry box to display number and arithmatic operator

    eq = tk.StringVar()
    entry = ttk.Entry(top,width = 40, state = "readonly",background = "red", textvariable = eq)
    entry.grid(row=0, column=10, ipadx = 6, ipady = 8)
    entry.focus()
    
btn7 = ttk.Button(top, text = '7' , width = 5 ,  command = lambda : press(7) )

btn7.grid(row = 1 , column = 0 ,ipady = 4 , ipadx = 2)    
    
btn8 = ttk.Button(top, text = '8' , width = 5 ,  command = lambda : press(8))
btn8.grid(row = 1 , column = 1 ,ipady = 4, ipadx = 2)

btn9 = ttk.Button(top, text = '9' , width = 5 ,  command = lambda : press(9) )
btn9.grid(row = 1 , column = 2,ipady = 4, ipadx = 2)

btnmines = ttk.Button(top, text = '-' , width = 8 ,  command = lambda : press('-') )
btnmines.grid(row = 1 , column = 3 , ipady = 3, ipadx = 2)


    

        
        
