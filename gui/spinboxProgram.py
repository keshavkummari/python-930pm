from tkinter import *

master = Tk()
master.geometry("500x500")
w = Spinbox(master, from_=0, to=10)
w.pack()

mainloop()
