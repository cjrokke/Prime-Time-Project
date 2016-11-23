# Project Name: Prime-Time-Project
# File: GUI.py
# NOTE: this is our graphical user interface
# import index
from Tkinter import *  # Importing the Tkinter (tool box) library
# might need be "tkinter"
#from Slow_Brain import *
#from Fast_Brain import *

# add import brain


def primeCheck(event):
    # if prime bool true
    # flash button using fg bg
    # else flash button using fg bg
    # refresh FB time sb time
    pass


def sbTime():
    return "yeo"  # placeholder string


def fbTime():
    return "test"  # placeholder string

root = Tk()  # Creats object root that has properties for the window. Access via .instr
# configuration portion
root.font = ('Verdana', '20', 'bold')  # changes the font for ALL text belonging to root

dummyEvent = FALSE

entry1 = Entry(root, text="test").pack
SBtime = Label(root, text="test").pack
FBtime = Label(root, text="test").pack
PLabel = Label(root, text="Placeholder Prime/Notprime", font="Times 19 bold").pack
Ybutton = Button(root, text="Prime", fg='blue', bg='green').pack()  # currently packed just to populate the message box
Nbutton = Button(root, text="Not-Prime", fg='black', bg='red').pack()  # need to link to functions


root.mainloop()  # Execute the main event handler
