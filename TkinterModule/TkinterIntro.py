'''
> Python provides the standard library Tkinter for creating the graphical user interface for desktop based applications.
> import the Tkinter module.
> Create the main application window.
> Add the widgets like labels, buttons, frames, etc. to the window.
> Call the main event loop so that the actions can take place on the user's computer screen.
'''
from tkinter import *  
#creating the application main window.   
top = Tk() #Tk() is a function which is used to create the main application window. 
#Entering the event main loop  
top.mainloop() #mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event till the window is not closed.