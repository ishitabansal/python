import tkinter as tk
from functools import partial

def call_result(label_result, n1, n2):
     num1 = (n1.get())
     num2 = (n2.get())
     result = int(num1)+int(num2)
    
     label_result.config(text="Result = %d" % result)
    
     return

top = tk.Tk()
top.geometry("440x200+100+200")

top.title("Calculator")
number1= tk.StringVar()
number2 = tk.StringVar()

labelnum1 = tk.Label(top,text="A").grid(row=1,column=0)
labelnum2 = tk.Label(top,text="B").grid(row=2,column=0)

labelresult = tk.Label(top)

labelresult.grid(row=7,column=2)

