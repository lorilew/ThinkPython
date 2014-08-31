import math

def square_root(a,x):
    """
    a: find the sqrt of a
    x: estimate
    """
    y = (x + a/x)/2
    while abs(y-x)> 0.0000001:
        x = y
        y = (x + a/x)/2
        print("sqrt:",y)

def square_root_2(a,x):
    y = (x + a/x)/2
    while True:
        x = y
        y = (x + a/x)/2
        print("sqrt2:",y)
        if abs(y-x)< 0.0000001:
            break

n = 78
g = 7

square_root(n,g)
square_root_2(n,g)
print("Ans:", math.sqrt(n))
    
