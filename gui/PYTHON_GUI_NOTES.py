'''**************************************************************************'''
# GUI Programming (Tkinter) :

Python provides various options for developing graphical user interfaces (GUIs). 

Tkinter: Tkinter is the Python interface to the Tk GUI toolkit shipped with Python. 

wxPython: This is an open-source Python interface for wxWidgets GUI toolkit. 

PyQt:This is also a Python interface for a popular cross-platform Qt GUI library. 

JPython: JPython is a Python port for Java which gives Python scripts seamless
access to Java class libraries on the local machine http://www.jython.org

There are many other interfaces available

'''**************************************************************************'''
# Tkinter Programming :

Tkinter is the standard GUI library for Python. 

Python when combined with Tkinter provides a fast and easy way to create GUI applications. 

Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.

Creating a GUI application using Tkinter is an easy task. 

	1. Import the Tkinter module.

	2. Create the GUI application main window.

	3. Add one or more of the above-mentioned widgets to the GUI application.

	4. Enter the main event loop to take action against each event triggered by the user.
'''**************************************************************************'''
# Example: 

#!/usr/bin/python3

import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
top = tkinter.Tk()
# Code to add widgets will go here...
top.mainloop()

'''**************************************************************************'''
# Tkinter Widgets :

Tkinter provides various controls, such as buttons, labels and text boxes used in a GUI application. 

These controls are commonly called widgets.

There are currently 15 types of widgets in Tkinter. 

We present these widgets as well as a brief description in the following table :

-----------------------------------------------------------------------------------
Sno		Operator		Description
-----------------------------------------------------------------------------------
1. Button	    :	The Button widget is used to display buttons in your application.
2. Canvas	    :	The Canvas widget is used to draw shapes, such as lines, ovals, 
					polygons and rectangles, in your application.
3. Checkbutton	:	The Checkbutton widget is used to display a number of options as checkboxes. 
					The user can select multiple options at a time.
4. Entry		:	The Entry widget is used to display a single-line text field for accepting values from a user.
5. Frame		:	The Frame widget is used as a container widget to organize other widgets.
6. Label		:	The Label widget is used to provide a single-line caption for other widgets. It can also contain images.
7. Listbox		:	The Listbox widget is used to provide a list of options to a user.
8. Menubutton	:	The Menubutton widget is used to display menus in your application.
9. Menu			:	The Menu widget is used to provide various commands to a user. 
					These commands are contained inside Menubutton.
10. Message		:	The Message widget is used to display multiline text fields for accepting values from a user.
11. Radiobutton	:	The Radiobutton widget is used to display a number of options as radio buttons. 
					The user can select only one option at a time.
12. Scale		:	The Scale widget is used to provide a slider widget.
13. Scrollbar	:	The Scrollbar widget is used to add scrolling capability to various widgets, such as list boxes.
14. Text		:	The Text widget is used to display text in multiple lines.
15. Toplevel	:	The Toplevel widget is used to provide a separate window container.
16. Spinbox		:	The Spinbox widget is a variant of the standard Tkinter Entry widget, 
					which can be used to select from a fixed number of values.
17. PanedWindow	:	A PanedWindow is a container widget that may contain any number of panes, 
					arranged horizontally or vertically.
18. LabelFrame	:	A labelframe is a simple container widget. 
					Its primary purpose is to act as a spacer or container for complex window layouts.
19. tkMessageBox:	This module is used to display message boxes in your applications.
'''**************************************************************************'''
# WIDGETS:

1. Tkinter Button :

The Button widget is used to add buttons in a Python application. 

These buttons can display text or images that convey the purpose of the buttons. 

You can attach a function or a method to a button which is called automatically when you click
the button.

# Syntax : w = Button ( master, option=value, ... )

master: This represents the parent window.

options: Here is the list of most commonly used options for this widget. 
         These options can be used as key-value pairs separated by commas.
----------------------------------------------------------------------------------		 
SNO	Option		Description
----------------------------------------------------------------------------------
1	activebackground	:	Background color when the button is under the cursor.
2	activeforeground	:	Foreground color when the button is under the cursor.
3	bd					:	Border width in pixels. Default is 2.
4	bg					:	Normal background color.
5	command	: Function or method to be called when the button is clicked.
6	fg					:	Normal foreground (text) color.
7	font	:	Text font to be used for the button's label.
8	height	:	Height of the button in text lines (for textual buttons) or pixels (for images).
9	highlightcolor	: The color of the focus highlight when the widget has focus.
10	image	:	Image to be displayed on the button (instead of text).
11	justify	:	How to show multiple text lines: LEFT to left-justify each line; CENTER to center them; or RIGHT to right-justify.
12	padx	:	Additional padding left and right of the text.
13	pady	:	Additional padding above and below the text.
14	relief	:	Relief specifies the type of the border.
                        Some of the values are SUNKEN, RAISED, GROOVE, and RIDGE.
15	state	:	Set this option to DISABLED to gray out the button and make it unresponsive. Has the value ACTIVE when the mouse is over it. Default is NORMAL.
16	underline	:	Default is -1, meaning that no character of the text on the button will be underlined. If nonnegative, the corresponding text character will be underlined.
17	width	:	Width of the button in letters (if displaying text) or pixels (if displaying an image).
18	wraplength	:	If this value is set to a positive number, the text lines will be wrapped to fit within this length.
'''**************************************************************************'''		 
# Methods:

Following are commonly used methods for this widget:

flash()		: Causes the button to flash several times between active and normal colors. 
		Leaves the button in the state it was in originally. Ignored if the button is disabled.
invoke()	: Calls the button's callback, and returns what that function returns. 
			  Has no effect if the button is disabled or there is no callback.

Example
Try the following example yourself −

# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def helloCallBack():
   msg=messagebox.showinfo( "Hello Python", "Hello World")

B = Button(top, text ="Hello", command = helloCallBack)
B.place(x=50,y=50)
top.mainloop()
			  
'''**************************************************************************'''
Let us study these widgets in detail :

# Standard attributes:

Let us take a look at how some of their common attributes.such as sizes, colors and fonts are specified.

Dimensions

Colors

Fonts

Anchors

Relief styles

Bitmaps

Cursors

Let us study them briefly

'''**************************************************************************'''
# Geometry Management :

All Tkinter widgets have access to specific geometry management methods, 
which have the purpose of organizing widgets throughout the parent widget area. 

Tkinter exposes the following geometry manager classes: pack, grid, and place.

The pack() Method - This geometry manager organizes widgets in blocks
before placing them in the parent widget.

The grid() Method - This geometry manager organizes widgets in a table-like
structure in the parent widget.

The place() Method -This geometry manager organizes widgets by placing them in a
specific position in the parent widget.
'''**************************************************************************'''


'''**************************************************************************'''
