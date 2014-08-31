from TurtleWorld import *

def koch(t, length):
    if length<4:
        fd(t,length/3)
    else:
        angle = 60
        koch(t,length/2)
        lt(t,angle)
        koch(t,length/2)
        rt(t,angle*2)
        koch(t,length/2)
        lt(t,angle)
        koch(t,length/2)

world = TurtleWorld()
t= Turtle()
t.delay = 0.01

length = 100
angle = 60
n = 3

koch(t,100)

      
