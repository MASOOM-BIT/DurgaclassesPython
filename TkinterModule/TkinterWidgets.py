'''
There are various widgets like button, canvas, checkbutton, entry, etc. that are used to build the python GUI applications.


1:Button
The Button is used to add various kinds of buttons to the python application.

2:Canvas
The canvas widget is used to draw the canvas on the window.

3: Checkbutton
The Checkbutton is used to display the CheckButton on the window.

4:Entry
The entry widget is used to display the single-line text field to the user. It is commonly used to accept user values.

5:Frame
It can be defined as a container to which, another widget can be added and organized.

6:Label
A label is a text used to display some message or information about the other widgets.

7:ListBox
The ListBox widget is used to display a list of options to the user.

8:Menubutton
The Menubutton is used to display the menu items to the user.

9:Menu
It is used to add menu items to the user.

10: Message
The Message widget is used to display the message-box to the user.

11:Radiobutton
The Radiobutton is different from a checkbutton. Here, the user is provided with various options and the user can select only one option among them.

12:Scale
It is used to provide the slider to the user.

13:Scrollbar
It provides the scrollbar to the user so that the user can scroll the window up and down.

14:Text
It is different from Entry because it provides a multi-line text field to the user so that the user can write the text and edit the text inside it.

14:Toplevel
It is used to create a separate window container.

15:Spinbox
It is an entry widget used to select from options of values.

16:PanedWindow
It is like a container widget that contains horizontal or vertical panes.

17:LabelFrame
A LabelFrame is a container widget that acts as the container

18:MessageBox
This module is used to display the message-box in the desktop based applications.
'''
from tkinter import *
# parent = Tk()  
# redbutton = Button(parent, text = "Red", fg = "red")  
# redbutton.pack( side = LEFT)  
# greenbutton = Button(parent, text = "Black", fg = "black")  
# greenbutton.pack( side = RIGHT )  
# bluebutton = Button(parent, text = "Blue", fg = "blue")  
# bluebutton.pack( side = TOP )  
# blackbutton = Button(parent, text = "Green", fg = "red")  
# blackbutton.pack( side = BOTTOM)  
# parent.mainloop()

parent = Tk()  
name = Label(parent,text = "Name").grid(row = 0, column = 0)  
e1 = Entry(parent).grid(row = 0, column = 1)  
password = Label(parent,text = "Password").grid(row = 1, column = 0)  
e2 = Entry(parent).grid(row = 1, column = 1)  
submit = Button(parent, text = "Submit").grid(row = 4, column = 0)  
parent.mainloop()  