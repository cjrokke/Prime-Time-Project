# Project Name: Prime-Time-Project
# File: GUI.py
# NOTE: this is our graphical user interface
import index
from Tkinter import *  # Importing the Tkinter (tool box) library
# might need be "tkinter"
from Slow_Brain import *
from Fast_Brain import *
def primeCheck(event):
    value = entry1.get()
    #send value to function index given
    #val = call indexgui
    return

def sbTime():
    return "yeo"  # placeholder string


def fbTime():
    return "test"  # placeholder string

root = Tk()  # Creats object root that has properties for the window. Access via .instr
# configuration portion
root.font = ('Verdana', '20', 'bold')  # changes the font for ALL text belonging to root

dummyEvent = FALSE

SBtime = Label(root, text="test1").grid(row=1, sticky = W)
FBtime = Label(root, text="test2").grid(row=1,sticky = E)

entry1 = Entry(root, text="test3").grid(row=2)
PLabel = Label(root, text="Enter Value to Check", font="Times 10").grid(row=3)
Ybutton = Button(root, text="Prime", fg='blue', bg='green').grid(row=0,  sticky=W)  # currently packed just to populate the message box
Nbutton = Button(root, text="Not-Prime", fg='black', bg='red').grid(row=0, sticky=E)# need to link to functions

entry1.bind("<return>", primeCheck)

root.mainloop()  # Execute the main event handler
