from tkinter import *  
  
def selection():  
   selection = "You selected the option " + str(radio.get())  
   label.config(text = selection)  
  
top = Tk()  
top.geometry("300x150")  
radio = IntVar()  
lbl = Label(text = "Favourite programming language:")  
lbl.pack()  
R1 = Radiobutton(top, text="C", variable=radio, value=1,  
                  command=selection)  
R1.pack( anchor = W )  
  
R2 = Radiobutton(top, text="C++", variable=radio, value=2,  
                  command=selection)  
R2.pack( anchor = W )  
  
R3 = Radiobutton(top, text="Java", variable=radio, value=3,  
                  command=selection)  
R3.pack( anchor = W)  
  
label = Label(top)  
label.pack()  
top.mainloop()  


<------------------2nd example-------------------->
from tkinter import *

def click_me():
    print(i.get())
top=Tk(className='RadioButton')
i= IntVar()

r1 = Radiobutton(top,text="C",value=1,variable=i,font=(None,20))
r2 = Radiobutton(top,text="C++",value=2,variable=i,font=(None,20))
r3 = Radiobutton(top,text="java",value=3,variable=i,font=(None,20))
r1.pack()
r2.pack()
r3.pack()

btn = Button(top,text="check",command=click_me)


btn.pack()
top.geometry("300x300+220+120")
top.mainloop()
