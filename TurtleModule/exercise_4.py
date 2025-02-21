import turtle


def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

t=turtle.Turtle()
polygon(t,20,15)
turtle.mainloop()