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
    entry = ttk.Entry(top,width = 40, state = "readonly",background = "green", textvariable = eq)
    entry.grid(row=0, column=10, ipadx = 6, ipady = 8)
    entry.focus()
   
#add some button in the frame

btn7 = ttk.Button(top, text = '7' , width = 5 ,  command = lambda : press(7) )

btn7.grid(row = 1 , column = 0 ,ipady = 4 , ipadx = 2)    
    
btn8 = ttk.Button(top, text = '8' , width = 5 ,  command = lambda : press(8))
btn8.grid(row = 1 , column = 1 ,ipady = 4, ipadx = 2)

btn9 = ttk.Button(top, text = '9' , width = 5 ,  command = lambda : press(9) )
btn9.grid(row = 1 , column = 2,ipady = 4, ipadx = 2)

btnmines = ttk.Button(top, text = '-' , width = 8 ,  command = lambda : press('-') )
btnmines.grid(row = 1 , column = 3 , ipady = 3, ipadx = 2)

btnmul = ttk.Button(top, text = '*' , width = 8 ,  command = lambda : press("*") )
btnmul.grid(row = 1 , column = 4 , ipady = 3, ipadx = 2)

btn4 = ttk.Button(top, text = '4' , width = 5 ,  command = lambda : press(4) )
btn4.grid(row = 2 , column = 0 ,ipady = 4 , ipadx = 2)

btn5 = ttk.Button(top, text = '5' , width = 5 ,  command = lambda : press(5) )
btn5.grid(row = 2 , column = 1 ,ipady = 4, ipadx = 2)

btn6 = ttk.Button(top, text = '6' , width = 5 ,  command = lambda : press(6) )
btn6.grid(row = 2 , column = 2,ipady = 4, ipadx = 3)

btnplus = ttk.Button(top, text = '+' , width = 8 ,  command = lambda : press("+") )
btnplus.grid(row = 2 , column = 3,ipady = 3, ipadx = 2)

btndiv = ttk.Button(top, text= '/' , width = 8 , command = lambda : press("/") )
btndiv.grid(row = 2 , column = 4, ipady = 3, ipadx = 2)

btn3 = ttk.Button(top, text="3" , width = 5 , command = lambda : press(3) )
btn3.grid(row =3 , column = 0, ipady = 4, ipadx = 2)

btn2 = ttk.Button(top, text="2" , width = 5 , command = lambda : press(2) )
btn2.grid(row =3 , column = 1, ipady = 4, ipadx = 2)

btn1 = ttk.Button(top, text="1" , width = 5 , command = lambda : press(1) )
btn1.grid(row =3 , column = 2, ipady = 4, ipadx = 2)

btn0 = ttk.Button(top, text="0" , width = 8 , command = lambda : press(0) )
btn0.grid(row =3 , column = 3, ipady = 3, ipadx = 2)

btnequ = ttk.Button(top, text="=" , width = 8 , command = press1 )
btnequ.grid(row =3, column = 4, ipady=3 , ipadx = 2)

btnclr = ttk.Button(top, text="Clear",width = 41, command = clear)
btnclr.grid(row=4, columnspan = 6, ipady=4, ipadx=2)




top.mainloop()
 

    

        
        
