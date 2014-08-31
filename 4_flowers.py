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
    n = 200
    length = circumference / n
    polygon(t,n,length,a)

def petal(t,r,a):
    for i in range(2):
       arc(t,r,a)
       lt(t,180-a)

def flower(t,r,a,n):
    """
    Draws a flower with n petals 
    t:turle
    r:radius of arc-circle
    a:angle of arc-circle
    n:number of petals
    """
    for i in range(n):
        petal(t,r,a)
        lt(t,360/n)


world = TurtleWorld()
bob= Turtle()
bob.delay = 0.005
flower(bob,100,45,10)



print("Finished")

wait_for_user()
