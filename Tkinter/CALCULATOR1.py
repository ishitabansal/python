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
