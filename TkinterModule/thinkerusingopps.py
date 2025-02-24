from tkinter import *
class Demo:
    def __init__(self,rootone):
        frame=Frame(rootone)
        frame.pack()

        self.print_button=Button(frame,text='Click Me',command=self.print_message())
        self.print_button.pack()

        self.quitbutton=Button(frame,text='Exit',command=frame.quit)
        self.quitbutton.pack()

    
    def print_message(self):
        print('Button Clicked')



root=Tk()
d=Demo(root)
root.mainloop()