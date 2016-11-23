# Project Name: Prime-Time-Project
# File: GUI.py
# NOTE: this is our graphical user interface
#import index
from Tkinter import *  # Importing the Tkinter (tool box) library
from index_GUI_test import*

def primeCheck(event):

    if re.search('[a-zA-Z]', entry1.get()):
        print("invalid entry")
        return
    if brain(int(entry1.get())):
        #toggle prime

        pass
    else:
        #toggle not-prime
        pass

def sbTime():
     pass   # placeholder string


def fbTime():
    return "test"  # placeholder string

root = Tk()  # Creats object root that has properties for the window. Access via .instr
# configuration portion
root.font = ('Verdana', '20', 'bold')  # changes the font for ALL text belonging to root

dummyEvent = FALSE

SBtime = Label(root, text="test1").grid(row=1, sticky = W)
FBtime = Label(root, text="test2").grid(row=1,sticky = E)

entry1 = Entry(root)
entry1.grid(row=2)
PLabel = Label(root, text="Enter Value to Check", font="Times 10").grid(row=3)
Pbutton = Button(root, text="Prime", fg='Black', bg='white').grid(row=0,  sticky=W)  # currently packed just to populate the message box
NPbutton = Button(root, text="Not-Prime", fg='black', bg='white').grid(row=0, sticky=E)# need to link to functions

entry1.bind('<Return>', primeCheck)

root.mainloop()  # Execute the main event handler
