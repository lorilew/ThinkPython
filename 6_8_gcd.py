import math

def gcd(a, b):
    a = int(a)
    print("gcd",a,b)
    if a<0 or b<0:
        return None
    elif (not isinstance(a, int)) or (not isinstance(b, int)):
        return None
    elif b==a:
        return a
    elif b==0:
        return a
    else:
        r = a%b
        return gcd(b,r)
        

print(gcd(4,4))
print(gcd(2,4))
print(gcd(9,27))
print(gcd(90, 27))
