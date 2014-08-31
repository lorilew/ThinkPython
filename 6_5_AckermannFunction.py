def ack(m,n):
    space = " " *(4*n)
    #print(space, "ack" ,m,n)
    
    if m==0:
        temp = n + 1
        #print(space, "returning n+1 =", temp)
        return temp
    elif m>0 and n==0:
        recurse = ack(m-1,1)
        return recurse
    elif m>0 and n>0:
        recurse = ack(m-1, ack(m,n-1))
        return recurse
    else:
        print("Only defined for positive values")

print (ack(3,4))
