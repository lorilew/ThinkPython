def compare(x,y):
    if x>y:
        return 1
    elif x==y:
        return 0
    else:
        return -1

x = input("x:")
y = input("y:")

print(compare(x,y))

