# !/usr/bin/python3
from tkinter import *

top = Tk()
top.geometry("500x500")

labelframe = LabelFrame(top, text="This is a LabelFrame")
labelframe.pack(fill="both", expand="yes")
 
left = Label(labelframe, text="Inside the LabelFrame")
left.pack()
 
top.mainloop()
