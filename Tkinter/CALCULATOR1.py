mport tkinter as tk

top= tk.Tk()

canvas1 = tk.Canvas(top, width = 330, height = 330)
canvas1.pack()

entry1 = tk.Entry(top) 
canvas1.create_window(210, 100, window=entry1)

entry2 = tk.Entry(top)
canvas1.create_window(210,140, window=entry2)

entry3 = tk.Entry(top)
canvas1.create_window(210,240, window=entry3)

label = tk.Label(top,text='Calculator')
label.config(font=('helvetica', 20))
canvas1.create_window(150,40,window=label)

label1 = tk.Label(top,text="ENTER VALUE 1 : ")
label1.config(font=('helvetica', 7))
canvas1.create_window(100,100,window=label1)

label2 = tk.Label(top,text="ENTER VALUE 2 : ")
label2.config(font=('helvetica', 7))
canvas1.create_window(100,140,window=label2)

label3 = tk.Label(top,text="RESULT : ")
label3.config(font=('helvetica', 10))
canvas1.create_window(100,240,window=label3)
