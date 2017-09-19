import turtle
import math

julian = turtle.Turtle()
julian.speed(0)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t, r, n):
    circumference = 2 * math.pi * r
    length = circumference / n
    polygon(t, length, n)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / 100

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def drawCenterCircle(width):
    julian.up()
    julian.setpos(0, -width)
    julian.down()
    circle(julian, width, 100)
    julian.up()
    julian.home()
    julian.down()

def firstShape(n, width):
    drawCenterCircle(width)

    julian.lt(60)
    polygon(julian, width, 3)

    for i in range(n):
        julian.lt(360/n)
        polygon(julian, width, 3)

    julian.up()
    julian.setpos(width/4, width/2)
    julian.down()
    circle(julian, width/4, 100)
    julian.up()

def secondShape(n, width):
    drawCenterCircle(width)

    arc(julian, 50, 180)


firstShape(4, 100)

turtle.mainloop()