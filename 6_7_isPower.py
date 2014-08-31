def is_power(a, b):
    a = int(a)
    print("is_power",a,b)
    if a<=0 or b<=0:
        return None
    elif (not isinstance(a, int)) or (not isinstance(b, int)):
        return None
    elif a==b:
        return True
    elif a%b==0:
        return is_power(a/b, b)
    else:
        return False

print
print(is_power(2,4))
print(is_power(4,4))
print(is_power(3**7,3))
