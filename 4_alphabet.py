import math

from TurtleWorld import *



def draw_a(t):
    lt(bob,80)
    fd(bob,100)
    lt(bob,180+20)
    fd(bob,50)
    lt(bob,180+80)
    fd(bob,15)
    bk(bob,15)
    lt(bob,180-80)
    fd(bob,50)
    


world = TurtleWorld()
bob= Turtle()
bob.delay = 0.005
draw_a(bob)
