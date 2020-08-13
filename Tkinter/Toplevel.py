from tkinter import *  
  
root = Tk()  
  
root.geometry("200x200")               
  
def open():  
    top = Toplevel(root)  
    top.mainloop()  
  

btn = Button(root, text = "open", command = open)              #create the button
  
btn.place(x=75,y=50)  
  
root.mainloop()  



#The toplevel widget is used when a python application needs to represent some extra information, pop-up, or the group of widgets on the new window.
# managed by the window manager
