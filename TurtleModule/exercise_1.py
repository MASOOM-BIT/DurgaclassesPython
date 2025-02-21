import turtle


def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

t=turtle.Turtle()
square(t)
turtle.mainloop()