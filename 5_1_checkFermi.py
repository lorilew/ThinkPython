"""EXAMPLE
def print_n(s,n):
    if n<=0:
        return
    print(s)
    print_n(s,n-1)

print_n("hello",2)
"""

def check_fermi(a,b,c,n):
    if n<=2:
        print("n must be more than 2")
    elif (a**n)+(b**n) == (c**n):
        print("Holy Smoke, Fermat was wrong!")
    else:
        
        print(str(n) + " - No, that doesn't work")


check_fermi(3,4,6,2)    
    
