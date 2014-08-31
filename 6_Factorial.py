def factorial(n):
    if not isinstance(n,int):
        return None
    elif n<0:
        return None
    elif n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

