import tkinter
from tkinter import *

win = Tk()
def pr():
    print("hii")   
win.geometry("400x400")
b = Button(win , text= "button" , command=pr , padx=30 , pady=20 , activebackground="blue" )
b.grid(row=1, column=4)
b2 = Button(win , text= "button2")
b2.grid(row=1, column=1)


win.mainloop()

