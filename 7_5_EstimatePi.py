import math

def factorial(n):
    if not isinstance(n,int):
        return None
    elif n<0:
        return None
    elif n==0:
        return 1
    else:
        return n*factorial(n-1)


def estimate_pi():
    sum = 0
    k=0
    while True:
        newTerm = ((factorial(4*k))*(1103 + 26390*k))/(((factorial(k))**4)*((396)**(4*k)))
        sum = sum + newTerm
        k += 1
        if newTerm<1e-15:
            break
    Inv_pi = (2*math.sqrt(2)/9801)*sum
    pi = 1/Inv_pi
    return pi

print(estimate_pi())        
