from tkinter import *   
  
top = Tk()  
  
top.geometry("200x200")  
  
#creating a simple canvas  
c = Canvas(top,bg = "pink",height = "200",width = 200)  
  
arc = c.create_arc((5,10,150,200),start = 0,extent = 150, fill= "white")  
  
c.pack()  
  
top.mainloop()  



# The canvas widget is used to add the structured graphics to the python application. It is used to draw the graph and plots to the python application.
