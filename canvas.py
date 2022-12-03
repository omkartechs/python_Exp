import tkinter
from tkinter import *

win = Tk()

c = Canvas(win, height=250, width=300, bg="blue")
coord=20,50,240,210
rc = c.create_arc(coord,start=90, extent=150, fill="red")
c.pack()

win.mainloop()

