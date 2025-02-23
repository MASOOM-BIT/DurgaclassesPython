from tkinter import *
window = Tk()
window.title("Durga classes Practice")
window.geometry('300x300')
label_1=Label(window,text='Hello World',fg='red',bg='white',font=('Arial',36))
label_1.pack()
def display():
    print('Button Clicked')
button=Button(window,text='Click Me',command=display)
button.pack()
window.mainloop()