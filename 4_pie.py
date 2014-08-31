import math

from TurtleWorld import *

def draw_wheel(t,n):
    for i in range(n):
        draw_spoke(t)
        draw_edge(t,n)

def draw_edge(t,n):
    theta = 360/n
    print(theta)

    phi = (180-theta)/2
    print(phi)

    length = 2*100*math.sin(theta/2*radian)/math.sin(90*radian)
    print(length)

    lt(bob,180-phi)
    fd(bob,length)
    lt(bob,180-phi)
    fd(bob,100)

def draw_spoke(t):
    lt(bob,180)
    fd(t,100)
    
    

world = TurtleWorld()
bob= Turtle()
bob.delay = 0.005
radian = 0.0174532925
draw_wheel(bob,3)




