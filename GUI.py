# Project Name: Prime-Time-Project
# File: GUI.py
# NOTE: this is our graphical user interface
import index
from Tkinter import *  # Importing the Tkinter (tool box) library
                        #might need be "tkinter"

root = Tk()  # Creats object root that has properties for the window. Access via .instr

# configuration portion
root.font = ('Verdana', '20', 'bold')   #changes the font for ALL text belonging to root

def pfunction():
    pass  # some code here hitting yes, pass just means no code is running here
    return


def npfunction():
    pass  # just pass this function for now
    return


Ybutton = Button(root, text="Prime", command=pfunction(), fg='blue', bg='green',).pack()            #currently packed just to populate the message box
Nbutton = Button(root, text="Not-Prime", command=npfunction(), fg='black', bg='red').pack()         #need to link to functions
                                                                                                    #above for functionallity

root.mainloop()  # Execute the main event handler


