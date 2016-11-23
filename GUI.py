# Project Name: Prime-Time-Project
# File: GUI.py
# NOTE: this is our graphical user interface
#import index
from Tkinter import *  # Importing the Tkinter (tool box) library
                        #might need be "tkinter"
from Slow_Brain import *
from Fast_Brain import *
#add import brain

root = Tk()  # Creats object root that has properties for the window. Access via .instr

# configuration portion
root.font = ('Verdana', '20', 'bold')   #changes the font for ALL text belonging to root

def primeTrue(event):
    pass
def primeFalse(event):
    pass



Ybutton = Button(root, text="Prime", fg='blue', bg='green',).pack()            #currently packed just to populate the message box
Nbutton = Button(root, text="Not-Prime",  fg='black', bg='red').pack()         #need to link to functions



#PLabel = Label(root, text =


root.mainloop()  # Execute the main event handler


