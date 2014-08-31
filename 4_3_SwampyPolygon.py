from TurtleWorld import *

def polygon(t, d):
    #d is external angle
    n = 360/d
    print(n)
    for i in range(int (n)*10):
        fd(t, 100)
        lt(t,d)

world = TurtleWorld()
bob= Turtle()
polygon(bob,100)

print("Finished")

wait_for_user()
