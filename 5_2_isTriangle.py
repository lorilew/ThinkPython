"""Write a function named is_triangle that takes three integers as arguments, and that prints
either “Yes” or “No,” depending on whether you can or cannot form a triangle from sticks
with the given lengths."""

def add_ints(a,b):
    return int(a)+int(b)

def is_triangle(a,b,c):
    if (add_ints(a,b))<=int(c):
        print("No")
    elif (add_ints(a,c))<=int(b):
        print("Noo")
    elif (add_ints(b,c))<=int(a):
        print("Nooo")
    else:
        print("yes")

        
a = input("Enter an integer a:")
b = input("Enter an integer b:")
c = input("Enter an integer c:")

is_triangle(a,b,c)
