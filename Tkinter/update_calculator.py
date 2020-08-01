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
