import turtle


def square(t,length,angle):
    for i in range(4):
        t.fd(length)
        t.lt(angle)

t=turtle.Turtle()
square(t,100,90)
turtle.mainloop()