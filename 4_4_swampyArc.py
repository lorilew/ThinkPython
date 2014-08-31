from TurtleWorld import *

def polygon(t, n, length, a):
    angle = 360.0 / n
    for i in range(int(n/(360/a))):
        fd(t, length)
        lt(t, angle)

def circle(t, r):
    arc(t,r,360)

def arc(t, r, a):
    circumference = 2 * 3.14 * r
    n = 50
    length = circumference / n
    polygon(t,n,length,a)


world = TurtleWorld()
bob= Turtle()
bob.delay = 0.01
arc(bob, 100, 270)

print("Finished")

wait_for_user()
