# !/usr/bin/python3
from tkinter import *


top = Tk()
top.geometry("500x500")
var = StringVar()
label = Label( top, textvariable=var, relief=RAISED )

var.set("Hey!? How are you doing?")
label.pack()
top.mainloop()
