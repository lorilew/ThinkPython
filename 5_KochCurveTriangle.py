from TurtleWorld import *

def koch(t, length):
    #change  < number to made simpler designs
    if length<20:
        fd(t,length/3)
    else:
        koch(t,length/2)
        lt(t,angle)
        koch(t,length/2)
        lt(t,angle*4)
        koch(t,length/2)
        lt(t,angle)
        koch(t,length/2)
    
world = TurtleWorld()
t= Turtle()
t.delay = 0.001

#change length for size of snowflake
length = 200
angle = 60
n = 3

koch(t,length)

rt(t,180 - angle)

koch(t,length)

rt(t,180 - angle)

koch(t,length)

      
