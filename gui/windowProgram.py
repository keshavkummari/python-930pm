# !/usr/bin/python3
from tkinter import *

top=Tk()
top.geometry("500x500")
m1 = PanedWindow()
m1.pack(fill=BOTH, expand=5)

right = Entry(m1, bd=5)
m1.add(right)

m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)

top = Scale( m2, orient=HORIZONTAL)
m2.add(top)

bottom = Button(m2, text="OK")
m2.add(bottom)

mainloop()
