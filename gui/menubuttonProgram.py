# !/usr/bin/python3

from tkinter import *

import tkinter

top = Tk()
top.geometry("500x500")

mb = Menubutton(top, text="COURSE", relief=RAISED )
mb.grid()
mb.menu  =  Menu (mb, tearoff = 0 )
mb["menu"]  =  mb.menu
    
mayoVar  = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton( label="Python",variable=mayoVar )
mb.menu.add_checkbutton ( label="Perl",variable=ketchVar )

mb.pack()
top.mainloop()
