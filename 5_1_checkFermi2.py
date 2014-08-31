"""Fermat's Last Theorem says that there are no integers
a,b,c such that a^n+b^n=c^n for any values of n greater
than 2. This code checks the theory."""

def check_fermi(a,b,c,n):
    if n<=2:
        print("n must be more than 2")
    elif (a**n)+(b**n) == (c**n):
        print("Holy Smoke, Fermat was wrong!")
    else:
        print((a**n)+(b**n))
        print("No, that doesn't work")

def input_int(s):
    """
    s is the variable name of the return value x.
    Function prompts user to input integer.
    Function converts to integer.
    """
    x = input("Enter an integer "+ s + ":\n")
    int(x)
    return x


a = input_int('a')
b = input_int('b')
c = input_int('c')
n = input_int('n')

check_fermi(int(a),int(b),int(c),int(n))    
