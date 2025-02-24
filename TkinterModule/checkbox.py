from tkinter import *

def on_button_toggle():
    if var.get() == 1:
        print("Checkbutton is selected")
    else:
        print("Checkbutton is deselected")

window = Tk()

# Creating a Checkbutton
var = IntVar()
checkbutton = Checkbutton(window, text="Check Me", variable=var, 
                             onvalue=1, offvalue=0, command=on_button_toggle)

# Setting options for the Checkbutton
checkbutton.config(bg="lightgrey", fg="blue", font=("Arial", 12), 
                   selectcolor="green", relief="raised", padx=10, pady=5)

# Adding a bitmap to the Checkbutton
checkbutton.config(bitmap="info", width=20, height=2)

# Placing the Checkbutton in the window
checkbutton.pack(padx=40, pady=40)

# Calling methods on the Checkbutton
checkbutton.flash()

checkbutton.mainloop()
